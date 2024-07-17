# PROJECT DATA LAKE 

## Mô hình project

![image](https://github.com/TuanMinh3006/Data-lake/assets/144102358/f2807342-2f6e-470b-9751-c65a21a566cb)

## Project này chia thành 3 phần: Thu thập dữ liệu, Xây dựng Data Lake, Analyzic  

## Mục đích: 
Tạo data lake có thể lưu trữ các file với các định dạng khác nhau, với các công cụ tự động thu thập và đẩy dữ liệu từ máy cá nhân lên nơi tập chung tổng của học viện , từ đây các thông tin có thể được trích xuất, chuyển đổi, sàng lọc đưa vào các hệ thống phân tích tiên tiến nhằm nắm bắt được tình hình học tập và giảng dạy ở học viện và tìm ra hướng phát triển tốt hơn cho học viện.

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

### 1.1. Xây dựng module thu thập điểm thi của sinh viên trường HVKTMM
-Mục tiêu: thu thập điểm thi kết thúc học phần của sinh viên trong trường trong 2 năm học 2022 – 2023 và 2023 – 2024 (từ đợt 1 học kì 1 cho đến đợt 1 học kì 2) để lưu trữ và phục vụ cho việc phân tích dữ liệu sau này.

-Đầu vào: [Trang web khảo thí của trường](https://ktdbcl.actvn.edu.vn/khao-thi/to-chuc-thi/ket-qua-thi.html?fbclid=IwZXh0bgNhZW0CMTEAAR2xloZngUWT3Xl5d4u0YOxp5DoIwBuGqt9KfAPz9SzoNz4n_Wm1ZrNff5M_aem_hVtwlsu5g3iDwhepiyi9Lg) 

  ![image](https://github.com/user-attachments/assets/a7d79f1f-1a3c-48b2-8d9a-2a7287da705a)


-Đầu ra:

![image](https://github.com/user-attachments/assets/38367b08-db5a-45e0-87bc-791542ee010f)
![image](https://github.com/user-attachments/assets/4c76cd33-8e46-434c-b57a-01b29ad621e8)
  
### 1.2. Lập trình module thu thập điểm tuyển sinh của trường HVKTMM
-Mục tiêu: thu thập điểm thi vào trường của các sinh viên trong 3 năm 2021, 2022, 2023 để lưu trữ và phục vụ cho việc phân tích dữ liệu sau này.

-Đầu vào: 
+ https://thi.tuyensinh247.com/danh-sach-trung-tuyen-hoc-vien-ky-thuat-mat-ma-nam-2021-c24a65727.html
+ https://thi.tuyensinh247.com/danh-sach-trung-tuyen-nam-2022-hoc-vien-ky-thuat-mat-ma-c24a71677.html
+ https://diemthi.tuyensinh247.com/danh-sach-trung-tuyen-dh-cd/hoc-vien-ky-thuat-mat-ma-KMA.html

-Đầu ra: 

![image](https://github.com/user-attachments/assets/f50a76f6-1d9d-404c-9af8-1a511af3ccd2)

### 1.3. Lập trình module thu thập điểm tốt nghiệp, điểm tiếng anh đầu vào/ra của trường HVKTMM
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

#### Nhóm các process để đẩy dữ liệu lên hồ dữ liệu:
Mục Tiêu: Tạo các luồng dữ liệu PUT , nhằm chuyển các dữ liệu đã crawl về máy local được vào hồ dữ liệu.

Cấu hình:

![image](https://github.com/user-attachments/assets/96626457-402d-491a-be2b-f7612dcb289a)

Đầu vào: Các file trên máy local

Đầu ra: Các file từ máy local đã được chuyển vào data lake và lưu trữ theo từng đặc điểm loại dữ liệu.
 
 ![image](https://github.com/user-attachments/assets/b1c5adf6-7a44-4b79-8461-887de5c0855f)


Kết quả thu được: Các file từ máy local đã được chuyển vào hồ dữ liệu và lưu trữ theo từng đặc điểm loại dữ liệu.
 
#### Nhóm các process để lấy dữ liệu từ  hồ dữ liệu:
Mục tiêu: Tạo các luồng dữ liệu GET, nhằm lấy dữ liệu trên hệ thống lưu trữ HDFS của hồ dữ liệu về các máy xử lý và phân tích dữ liệu.

Cấu hình:

![image](https://github.com/user-attachments/assets/7eecddbc-f3ac-45fa-85b3-43099845372e)

Đầu vào: Các file trên HDFS

Đầu ra : Các file đã được chuyển về máy xử lý và phân tích dữ liệu  và lưu trữ theo từng đặc điểm loại dữ liệu.

 ![image](https://github.com/user-attachments/assets/ef9b0ec0-eb05-40ab-afcc-20ac132dfd5f)


  
## Phần 3: Xử lý và trực quan hóa dữ liệu
-Mục đích: Xử lý và phân tích dữ liệu lấy từ hồ dữ liệu thành các dữ liệu hoặc biểu đồ có ích.
-Công cụ sử dụng: Thư viện fitz, pandas, mathplotlib, numpy (Python) 

### 3.1. Xây dựng module chuyển đổi điểm thi của sinh viên trương HVKTMM
-Mục Tiêu: Chuyển điểm điểm thi kết thúc học phần của sinh viên trong học viện từ dạng file .pdf sang file.csv

-Đầu vào: Các file điểm dạng PDF năm 2022-2023 và năm 2023-2024 

![image](https://github.com/user-attachments/assets/b44fd2b7-09e4-4349-9053-280d929edcdc)

![image](https://github.com/user-attachments/assets/069a21e8-7dd0-4505-a1de-25992f81fafb)
 
-Đầu ra: Các file điểm theo từng mã môn dạng CSV năm 2022-2023 và năm 2023-2024

 ![image](https://github.com/user-attachments/assets/b086539b-02c0-4820-96ea-ad7eaffa10cd)

 ![image](https://github.com/user-attachments/assets/456f4f47-8541-4445-8fbc-f6c1d31fe222)

### 3.2. Xây dựng module trực quan hóa dữ liệu điểm thi từng môn trường HVKTM
-Mục tiêu: Trực quan hóa dữ liệu bằng đồ thi thể hiện phổ điểm thi kết thúc học phần từng môn trường HVKTMM trong trong 2 năm học 2022 – 2023 và 2023 – 2024 (từ đợt 1 học kì 1 cho đến đợt 1 học kì 2) nhằm giúp thể hiện tổng quan về kết quả của toàn bộ học viện.
-Đầu vào: Các file điểm theo từng mã môn dạng csv năm 2022-2023 và năm 2023-2024
  
![image](https://github.com/user-attachments/assets/ec4b15e5-8058-486f-b244-2f859ed43179)

![image](https://github.com/user-attachments/assets/ed8087c5-5f64-4311-8f42-dac660c2de8f)

-Đầu ra : Các biểu đồ phổ điểm của từng mã môn , từng năm

 ![image](https://github.com/user-attachments/assets/560d1552-9c45-49b0-b04c-cf9681123c83)

 ![image](https://github.com/user-attachments/assets/d1edac8b-2af5-4563-a4d8-e961951d6177)

### 3.3. Xây dựng module trực quan hóa điểm trúng tuyển trung bình theo năm và ngành học của 2 phân hiệu của học viện.
-Mục tiêu: Xây dụng đồ thi thể hiện sự so sánh điểm trúng tuyển trung bình của đầu vào của học viện trong ba năm (2021, 2022, 2023) cho các ngành học.
-Đầu vào: Các file điểm trúng tuyển của sinh viên học viện có đuôi pdf theo các năm
 
 ![image](https://github.com/user-attachments/assets/ba895080-b328-44ff-b025-3e5d95152e50)

-Đầu ra: Đồ thị phổ điểm theo qua các năm 2021->2023

![image](https://github.com/user-attachments/assets/68d1558d-0682-481a-81e0-e3614532c66f)



