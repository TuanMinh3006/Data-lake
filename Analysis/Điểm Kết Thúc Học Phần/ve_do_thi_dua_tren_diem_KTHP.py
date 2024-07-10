# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:52:00 2024

@author: ADMIN
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


path_folder=r'/home/nifi/File_csv_and_do_thi/file_diem_KTHP_CSV'
path_do_thi=r'/home/nifi/File_csv_and_do_thi/Do_thi/KTHP'
os.makedirs(path_do_thi,exist_ok=True)
ext=('.csv')
list_path=[]
for path,dirc,files in os.walk(path_folder):
    for name in files:
        if name.endswith(ext):
            name_path=os.path.join(path, name)
        if 'phuc-khao' not in name_path:
            list_path.append(name_path)
for path in list_path:
    df = pd.read_csv(path)
    sorce=df['THI']
    tan_suat_diem=df['THI'].value_counts().sort_index()
    plt.figure(figsize=(20, 8))
    plt.bar(tan_suat_diem.index, tan_suat_diem.values,width=0.2, color='blue',label="Điểm")
    
    ma_hoc_phan=path.split('/')[-1][:-4]     #[:-4] để bỏ đuôi .csv
    ten_hk=path.split('/')[-2]
    ten_nam_hoc=path.split('/')[-3]
    
    plt.title(f'Biểu đồ phổ điểm thi của môn {ma_hoc_phan} - {ten_hk}')
    plt.xlabel('Điểm')
    plt.ylabel('Số lượng học sinh')
    # thêm chú thích 
    plt.legend(loc='upper right',title='Chú thích',frameon=True)
    
    #lưu sang dạng PNG
    path_folder_theo_hk=os.path.join(path_do_thi, ten_nam_hoc,ten_hk)
    os.makedirs(path_folder_theo_hk,exist_ok=True)
    path_save=os.path.join(path_folder_theo_hk,ma_hoc_phan+str('.png'))
    plt.savefig(path_save)
    plt.close()