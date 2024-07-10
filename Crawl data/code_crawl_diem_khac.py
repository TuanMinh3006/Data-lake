# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:32:09 2024

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
list_of_pdf= []
list1=[]
tables=soup.find_all('table')
table_diem=tables[1]
rows=table_diem.find_all('tr')
rows.pop(0)
for row in rows:
    o=row.find_all('td')
    title=str(o[1].contents[0])
    list1.append(title)
    links=row.find_all('a')
    for link in links:
        href=link.get('href')
        
        if href and href.endswith('.pdf'):
            full_url = urljoin(url, href)  # Join base URL with relative URL
            list_of_pdf.append([title,full_url])

#Lưu vào folder  
save_folder=r'/home/nifi/Data_crawl/Diem_khac'

os.makedirs(save_folder,exist_ok=True) # Tạo save_folder nếu chưa tồn tại 

for pdf in list_of_pdf:
    pdf_response = requests.get(pdf[1])
    pdf_name = os.path.basename(pdf[1])  # lấy tên của các file pdf
   
    
    url_folder = os.path.join(save_folder, pdf[0]) # tạo đường dẫn folder cụ thể theo title
    os.makedirs(url_folder,exist_ok=True) # Tạo folder mới với đường dẫn cụ thể theo title
    
    
    pdf_path = os.path.join(url_folder, pdf_name) # tạo đường dẫn cụ thể 
    with open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(pdf_response.content)

    print(f'Downloaded: {pdf_name}')