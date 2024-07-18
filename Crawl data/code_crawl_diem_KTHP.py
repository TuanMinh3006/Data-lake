# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:34:07 2024

@author: ADMIN
"""


import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url= 'https://ktdbcl.actvn.edu.vn/khao-thi/to-chuc-thi/ket-qua-thi.html'
read=requests.get(url)
html_content=read.content
soup=BeautifulSoup(html_content,'html.parser')
list_of_pdf= set()
tables=soup.find_all('table')
table_diem=tables[0]
links=table_diem.find_all('a')
for link in links:
    href=link.get('href')
    if href and href.endswith('.pdf'):
        full_url = urljoin(url, href)  # Join base URL with relative URL
        list_of_pdf.add(full_url)

#Lưu vào folder  

save_folder=r'/home/nifi/Data_crawl/Diem_KTHP'

os.makedirs(save_folder,exist_ok=True) # Tạo save_folder nếu chưa tồn tại 

for pdf_link in list_of_pdf:
    pdf_response = requests.get(pdf_link)
    pdf_name = os.path.basename(pdf_link)  # lấy tên của các file pdf
   
    year=pdf_name[0:9]
    year_folder = os.path.join(save_folder, year) # tạo đường dẫn folder cụ thể theo năm
    os.makedirs(year_folder,exist_ok=True) # Tạo folder mới với đường dẫn cụ thể theo năm
    
    
    pdf_path = os.path.join(year_folder, pdf_name) # tạo đường dẫn cụ thể 
    with open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(pdf_response.content)

    print(f'Downloaded: {pdf_name}')
