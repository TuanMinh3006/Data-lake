# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:33:36 2024

@author: ADMIN
"""

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def crawl_file_trung_tuyen(url,year):
    read=requests.get(url)
    html_content=read.content
    soup=BeautifulSoup(html_content,'html.parser')
    list_of_pdf= set()
    
    links= soup.find_all('a')
    for link in links:
        href=link.get('href')
        if href and href.endswith('.pdf'):
            full_url = urljoin(url, href)  # Join base URL with relative URL
            list_of_pdf.add(full_url)
    
    #Lưu vào folder  
    
    save_folder=r'/home/nifi/Data_crawl/Diem_tuyen_sinh'
    
    os.makedirs(save_folder,exist_ok=True) # Tạo save_folder nếu chưa tồn tại 
    
    
    
    for pdf_link in list_of_pdf:
        pdf_response = requests.get(pdf_link)
        pdf_name = os.path.basename(pdf_link)  # lấy tên của các file pdf
        ten=pdf_name.split('.')[0]
        
        
        pdf_path = os.path.join(save_folder, ten+str(year)+'.pdf') # tạo đường dẫn cụ thể 
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
    
        print(f'Downloaded: {pdf_name}')


list_url=[]
list_url.append(['https://thi.tuyensinh247.com/danh-sach-trung-tuyen-hoc-vien-ky-thuat-mat-ma-nam-2021-c24a65727.html','2021'])
list_url.append(['https://thi.tuyensinh247.com/danh-sach-trung-tuyen-nam-2022-hoc-vien-ky-thuat-mat-ma-c24a71677.html','2022'])
list_url.append(['https://diemthi.tuyensinh247.com/danh-sach-trung-tuyen-dh-cd/hoc-vien-ky-thuat-mat-ma-KMA.html','2023'])
for url,year in list_url:
    crawl_file_trung_tuyen(url,year)