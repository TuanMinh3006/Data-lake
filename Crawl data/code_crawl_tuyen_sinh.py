# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:34:35 2024

@author: ADMIN
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import random
import os

# Function to write data to CSV
def write_csv(file_name, data):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Link', 'Title', 'Description'])
        for row in data:
            writer.writerow([row.get('link'), row.get('title'), row.get('description')])

# Function to search for recruitment plans in 2024
def search_recruitment_plans():
    url = 'https://www.google.com/search?q=xu+h%C6%B0%E1%BB%9Bng+tuy%E1%BB%83n+sinh+2024&oq=xu+h%C6%B0%E1%BB%9Bng+tuy%E1%BB%83n+sinh+2024&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCggCEAAYogQYiQUyCggDEAAYgAQYogQyCggEEAAYogQYiQUyCggFEAAYgAQYogQyCggGEAAYgAQYogTSAQg1Njc0ajBqOagCALACAQ&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    all_data = soup.find_all("div", {"class": "g"})

    data = []
    for i in range(len(all_data)):
        link_tag = all_data[i].find('a')
        if link_tag is not None:
            link = link_tag.get('href')
            if link and link.startswith('http') and 'aclk' not in link:
                entry = {"link": link}
                try:
                    entry["title"] = all_data[i].find('h3', {"class": "DKV0Md"}).text
                except:
                    entry["title"] = None
                try:
                    entry["description"] = all_data[i].find("div", {"class": "Hdw6tb"}).text
                except:
                    entry["description"] = None
                data.append(entry)

    # Đường dẫn lưu tệp
    folder_path = '/home/nifi/Data_crawl/Tai_lieu_tuyen_sinh/tuyen_sinh_2024'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_name = os.path.join(folder_path, 'recruitment_trends_' + str(random.randint(1, 1000)) + '_' + str(datetime.now().date()) + '.csv')
    write_csv(file_name, data)
    print("Download Done")

# Execute the function
search_recruitment_plans()