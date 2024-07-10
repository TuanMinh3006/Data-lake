# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:53:07 2024

@author: ADMIN
"""

# -*- coding: utf-8 -*-

import fitz
import pandas as pd
import os 
import matplotlib.pyplot as plt
import numpy as np

def chuyen_df(path):
    dfs=[]
    doc=fitz.open(path)
    
    path_pdf_name =path.split('/')[-1]
    pdf_name=path_pdf_name.split('.')[0]
    year=pdf_name[-4:]
    for page in doc:
        tabs=page.find_tables()
        if tabs.tables:
            df=pd.DataFrame(tabs[0].extract())
            dfs.append(df)
            
    df_tong_hop=dfs[0]
    dfs=dfs[1:]
    for df in dfs:
        df_tong_hop=pd.concat([df_tong_hop,df],axis=0,ignore_index=True)
    #Gắn tên column    
    df_tong_hop=df_tong_hop.dropna(how='any',axis=0)
    df_tong_hop.columns=df_tong_hop.iloc[0]
    df_tong_hop=df_tong_hop[1:]
    
    #Sửa lý các value dư thừa
    df_tong_hop=df_tong_hop.replace('',None)
    df_tong_hop=df_tong_hop.replace('STT',None )
    df_tong_hop=df_tong_hop.dropna(how='any',axis=0)
    #reset lại index
    df_tong_hop.reset_index(drop=True, inplace=True)
    
    #Sửa 1 ô ghi mã ngành sai 
    df_tong_hop=df_tong_hop.replace('N7480201KMP','7480201KMP' )
    df_tong_hop['Năm']=year
    #Nhóm file theo mã ngành
    
    try:
        df_tong_hop.rename(columns={'Điểm TT':'Điểm trúng tuyển'},inplace=True)
        df_tong_hop.rename(columns={'Đ. Trúng tuyển':'Điểm trúng tuyển'},inplace=True)
        pass
    except :
        pass
    
    return df_tong_hop
    
def tinh_gia_tri_TB(df_tong_hop):
    df_tong_hop['Điểm trúng tuyển']=df_tong_hop['Điểm trúng tuyển'].astype(float)
    diem_tb=df_tong_hop.groupby(['Mã ngành','Năm'])['Điểm trúng tuyển'].mean().reset_index()
    diem_tb['Điểm trúng tuyển']=diem_tb['Điểm trúng tuyển'].apply(lambda x : round(x,2))
    return diem_tb

def gop_data_frame(list_df,df_tong_gop):
    column_can_lay=['Họ Tên','Mã ngành','Năm','Điểm trúng tuyển']
    for df in list_df:
        df_new=df[column_can_lay]
        df_tong_gop=pd.concat([df_tong_gop,df_new],ignore_index=True)
    return df_tong_gop


#Chuyển các file pdf sang csv 
list_df=[]

path_folder=r'/home/nifi/Data_From_HDFS/Diem_tuyen_sinh'
list_file=os.listdir(path_folder)
for name in list_file:
    path_file=os.path.join(path_folder,name)
    df=chuyen_df(path_file)
    list_df.append(df)



#Gộp các df thành một
name_columns=['Họ Tên','Mã ngành','Năm','Điểm trúng tuyển']
df_tong=pd.DataFrame(columns=name_columns)
 
df_tong=gop_data_frame(list_df,df_tong)
df_TB=tinh_gia_tri_TB(df_tong)
df_TB.info()

# Thêm cột Tên ngành
list_nganh={'7480201KMA':'Công nghệ thông tin KMA',
            '7480202KMA':'An toàn thông tin KMA',
            '7520207':'Kỹ thuật ĐTVT KMA',
            '7480201KMP':'Công nghệ thông tin KMP',
            '7480202KMP':'An toàn thông tin KMP'}

df_TB['Tên ngành']=df_TB['Mã ngành'].apply(lambda x : list_nganh[x])



#Điền bổ sung điểm của công nghệ thông tin KMP 2023 vì ko có số liệu
Diem_KMP_2023 = pd.DataFrame({
    'Mã ngành': ['7480201KMP'],
    'Năm': 2023,
    'Điểm trúng tuyển': [0.0],
    'Tên ngành': ['Công nghệ thông tin KMP']
})
#Group by dataFrame theo các năm
list_diem={}
grouped=df_TB.groupby('Năm')
for i in df_TB['Năm'].unique():
    df=grouped.get_group(i)
    if str(i) == '2023':
        df = pd.concat([df, Diem_KMP_2023], ignore_index=True)
    df =df.sort_values('Tên ngành')
    print(df)
    #Tạo từ điển có key là các năm và value là các dataframe chứa điểm ứng với năm (key)
    diem=list(df['Điểm trúng tuyển'])
    print(diem) 
    list_diem[i]=diem
#lấy các tên ngành sắp xếp thên bảng a-b
list_ten_cac_mon=sorted(df_TB['Tên ngành'].unique())


# Vẽ biểu đồ
plt.figure(figsize=(24, 9))
barWidth = 0.25

# Đặt vị trí cho các thanh ngang
r1 = np.arange(len(list_ten_cac_mon))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Tạo biểu đồ thanh ngang
plt.barh(r1, list_diem['2021'], color='blue', height=barWidth, edgecolor='grey', label='2021')
plt.barh(r2, list_diem['2022'], color='orange', height=barWidth, edgecolor='grey', label='2022')
plt.barh(r3, list_diem['2023'], color='green', height=barWidth, edgecolor='grey', label='2023')

# Điền các điểm chi tiết cho từng cột
for i in range(len(r1)):
    plt.text(list_diem['2021'][i] + 0.1, r1[i] - barWidth/4, str(list_diem['2021'][i]), color='black', va='center',fontsize=12)
    plt.text(list_diem['2022'][i] + 0.1, r2[i] - barWidth/4, str(list_diem['2022'][i]), color='black', va='center',fontsize=12)
    plt.text(list_diem['2023'][i] + 0.1, r3[i] - barWidth/4, str(list_diem['2023'][i]), color='black', va='center',fontsize=12)


# Gắn nhãn cho trục y
plt.yticks([r + barWidth for r in range(len(list_ten_cac_mon))], list_ten_cac_mon,fontsize=14)



# Thêm tiêu đề và chú thích
plt.xlabel('Điểm',fontsize=16)
plt.ylabel('Tên Ngành',fontsize=16)
plt.title('Điểm trúng tuyển theo năm và ngành',fontsize=18)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='x', linestyle='--')



path_folder_save=r'/home/nifi/File_csv_and_do_thi/file_diem_KTHP_CSV/Diem_tuyen_sinh'
os.makedirs(path_folder_save,exist_ok=True)
ten_path='Do_thi_diem_tuyen_sinh_qua_cac_nam.png'
path_save_do_thi=os.path.join(path_folder_save,ten_path)

plt.savefig(path_save_do_thi, format='png')

plt.close()