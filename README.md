# Data-lake

Project này chia thành 3 phần: Thu thập dữ liệu, Xây dựng Data Lake, Analyzic
![image](https://github.com/TuanMinh3006/Data-lake/assets/144102358/f2807342-2f6e-470b-9751-c65a21a566cb)


## Tech requirement
- [Python] - Yêu cầu từ phiên bản python 3.x
+ [Pip] - Yêu cầu trình quản lý gói pip
* [wget] - Dùng để tải các tệp nén chứa hadoop và nifi 
  
## Phần 1: Thu Thập dữ liệu

-Mục Đích: Thu thập dữ liệu bao gồm điểm kết thúc học phần, điểm thi đầu vào và các bài báo liên quan tới sinh viên về máy local

-Các Website lấy dữ liệu:
- https://ktdbcl.actvn.edu.vn/khao-thi/to-chuc-thi/ket-qua-thi.html?fbclid=IwZXh0bgNhZW0CMTEAAR2xloZngUWT3Xl5d4u0YOxp5DoIwBuGqt9KfAPz9SzoNz4n_Wm1ZrNff5M_aem_hVtwlsu5g3iDwhepiyi9Lg
+ https://thi.tuyensinh247.com/danh-sach-trung-tuyen-hoc-vien-ky-thuat-mat-ma-nam-2021-c24a65727.html
- https://thi.tuyensinh247.com/danh-sach-trung-tuyen-nam-2022-hoc-vien-ky-thuat-mat-ma-c24a71677.html
* https://diemthi.tuyensinh247.com/danh-sach-trung-tuyen-dh-cd/hoc-vien-ky-thuat-mat-ma-KMA.html
 
-Thư viện sử dụng: Request(Python), BeautifulSoup(Python)

### 3.2.1. Xây dựng module thu thập điểm thi của sinh viên trường HVKTMM
-Mục tiêu: thu thập điểm thi kết thúc học phần của sinh viên trong trường trong 2 năm học 2022 – 2023 và 2023 – 2024 (từ đợt 1 học kì 1 cho đến đợt 1 học kì 2) để lưu trữ và phục vụ cho việc phân tích dữ liệu sau này.

-Đầu vào: [Trang web khảo thí của trường](https://ktdbcl.actvn.edu.vn/khao-thi/to-chuc-thi/ket-qua-thi.html?fbclid=IwZXh0bgNhZW0CMTEAAR2xloZngUWT3Xl5d4u0YOxp5DoIwBuGqt9KfAPz9SzoNz4n_Wm1ZrNff5M_aem_hVtwlsu5g3iDwhepiyi9Lg) 

  ![image](https://github.com/user-attachments/assets/a7d79f1f-1a3c-48b2-8d9a-2a7287da705a)


-Đầu ra:

![image](https://github.com/user-attachments/assets/38367b08-db5a-45e0-87bc-791542ee010f)
![image](https://github.com/user-attachments/assets/4c76cd33-8e46-434c-b57a-01b29ad621e8)
  
### 3.2.2. Lập trình module thu thập điểm tuyển sinh của trường HVKTMM
-Mục tiêu: thu thập điểm thi vào trường của các sinh viên trong 3 năm 2021, 2022, 2023 để lưu trữ và phục vụ cho việc phân tích dữ liệu sau này.

-Đầu vào: 
+ https://thi.tuyensinh247.com/danh-sach-trung-tuyen-hoc-vien-ky-thuat-mat-ma-nam-2021-c24a65727.html
+ https://thi.tuyensinh247.com/danh-sach-trung-tuyen-nam-2022-hoc-vien-ky-thuat-mat-ma-c24a71677.html
+ https://diemthi.tuyensinh247.com/danh-sach-trung-tuyen-dh-cd/hoc-vien-ky-thuat-mat-ma-KMA.html

-Đầu ra: 

![image](https://github.com/user-attachments/assets/f50a76f6-1d9d-404c-9af8-1a511af3ccd2)

### 3.2.3. Lập trình module thu thập điểm tốt nghiệp, điểm tiếng anh đầu vào/ra của trường HVKTMM
-Mục tiêu: thu thập các đầu điểm khác (điểm tốt nghiệp, điểm tiếng anh đầu vào/ra, điểm phúc khảo,…) của sinh viên trường.

-Đầu vào: 
[Trang web khảo thí của trường](https://ktdbcl.actvn.edu.vn/khao-thi/to-chuc-thi/ket-qua-thi.html?fbclid=IwZXh0bgNhZW0CMTEAAR2xloZngUWT3Xl5d4u0YOxp5DoIwBuGqt9KfAPz9SzoNz4n_Wm1ZrNff5M_aem_hVtwlsu5g3iDwhepiyi9Lg)


![image](https://github.com/user-attachments/assets/8137f4db-3b99-4427-beb8-b90740e8ea0c)




-Đầu ra: 

![image](https://github.com/user-attachments/assets/29c5680f-2da6-4ec7-af2d-4d846b42442e)

 


 ## Phần 2: Xây dựng data lake
### 2.1: Xây dựng data lake
-Mục đích: Xây dựng data lake chứa các dữ liệu đã được thu thập về, nhằm mục đích cho các analyzic sau này.

-Công nghệ sử dụng: Hadoop
### 2.2: Xây dựng các luồng data để đẩy/lấy dữ liệu lên data lake
-Mục đích: Xây dựng các luồng dữ liệu đẩy tự động từ máy local lên data lake để lưu trữ. Và xây dựng các luồng dữ liệu tự động lấy dữ liệu từ máy data lake về máy local nhằm mục đích phân tích dữ liệu.

-Công nghệ sử dụng: Apache Nifi 



  
## Phần 3: Xử lý và trực quan hóa dữ liệu
-Mục đích: Tận dụng những dữ liệu thô(dạng PDF) đã có trong hồ dữ liệu chuyển đổi, xử lý một số dữ liệu bị missing thành các file dữ liệu .CSV hữu ích. Sử dụng Python để trực quan hóa các file .CSV thành các biểu đổ phổ điểm nhằm tìm ra các hướng giải dạy thích hợp cho từng môn học.

-Công cụ và thư viện sử dụng: pandas, numpy, matplotlib, fitz

-Đầu vào các 

