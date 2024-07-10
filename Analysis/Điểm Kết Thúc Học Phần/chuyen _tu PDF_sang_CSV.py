# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:44:25 2024

@author: ADMIN
"""
import fitz
import pandas as pd
import os

def extractct_course_title(page):
    text=page.get_text()
    for line in text.split('\n'):
        if 'Mã học phần' in line:
            return line.split(':')[1].strip()

def chuyen_df(path):
    # Lấy bảng 
    dfs=[]
    doc = fitz.open(path)
    for page in doc:
        tabs = page.find_tables()
        if tabs.tables:
            df = pd.DataFrame(tabs[0].extract())
            if df.iloc[0,0] == 'STT' or df.iloc[0,0] == 'TT':          # nếu ô đầu tiên trong chỉ mục bằng 'STT' và 'TT ' thì lấy làm tên colums
                df.columns=df.iloc[0] # lấy index đầu tiên làm tên các column
                df=df[1:]               # bỏ index đầu tiên
                df.reset_index(drop=True, inplace=True) # reset lại index
                if len(df.columns)>4:
                    dfs.append(df)
                
    
    #lấy title                
    course_names=[]
    
    for page_num in range(len(doc)):
        page=doc.load_page(page_num)
        course_name=extractct_course_title(page)
        if course_name!=None :
            course_names.append(course_name)
    
    
    #lấy set DISTINCT các mã học phần 
    list1=set(course_names)
    
    #Tạo  list df và tên tương ứng chứa tên mã học phần ứng với mỗi bảng
    list_df_va_name=[]
    for name,df in zip(course_names,dfs):
        list_df_va_name.append([name,df])
	
    
    # Tạo các df rỗng ứng với các mã học phần
    column_name=['STT','SBD','Mã sinh\nviên','Tên','Lớp','TP1','TP2','THI','TKHP','Chữ','Ghi chú']
    column_name_2=['STT','SBD','Mã sinh viên','Tên','Lớp','THI\n(lần 1)','Kết quả chấm\nPhúc khảo','TKHP','Chữ','Ghi chú']
    list_df_ouput={}
    for name in list1:
        if 'phuc-khao' in path:
            list_df_ouput[name]=pd.DataFrame(columns=column_name_2)
        else:
            list_df_ouput[name]=pd.DataFrame(columns=column_name)

    for i in range(len(list_df_va_name)):
        name = list_df_va_name[i][0]
        
        list_df_ouput[name]=pd.concat([list_df_ouput[name],list_df_va_name[i][1]],ignore_index=True)
    #Chuyển df sang định dạng csv và lưu
    save_folder= r'/home/nifi/File_csv_and_do_thi/file_diem_KTHP_CSV'   
    path_year=path.split('/')[-2]              
    path =path.split('/')[-1]
    name_url=path.split('.')[0]   # lấy tên file pdf
    
    ten_folder_cu_the=os.path.join(save_folder,path_year,name_url) #tạo url folder theo tên file pdf
    os.makedirs(ten_folder_cu_the,exist_ok=True)                   #Tạo folder nếu chưa có
    
    list_ma_hoc_phan=list(list_df_ouput.keys())                    #Lấy tên các mã học phần                              
    for i in list_ma_hoc_phan:
        name_file=str(i)+'.csv'                                    # tạo tên file csv
        ten_file_csv_cu_the=os.path.join(ten_folder_cu_the,name_file)
        list_df_ouput[i].to_csv(ten_file_csv_cu_the)
        

#Duyệt file trong folder
path_folder = r'/home/nifi/Data_From_HDFS/Diem_KTHP/nam-22-23'
list_file=os.listdir(path_folder)
for name_file in list_file:
    try:
        path_file=os.path.join(path_folder,name_file)
        chuyen_df(path_file)
        print(f'Transform {name_file} to .csv : Done')
        pass
    except :
        pass
    

path_folder = r'/home/nifi/Data_From_HDFS/Diem_KTHP/nam-23-24'
list_file=os.listdir(path_folder)
for name_file in list_file:
    try:
        path_file=os.path.join(path_folder,name_file)
        chuyen_df(path_file)
        print(f'Transform {name_file} to .csv : Done')
        pass
    except :
        pass
    

	