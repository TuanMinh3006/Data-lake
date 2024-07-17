# Data-lake

Project này chia thành 3 phần: Thu thập dữ liệu, Xây dựng Data Lake, Analyzic
![image](https://github.com/TuanMinh3006/Data-lake/assets/144102358/f2807342-2f6e-470b-9751-c65a21a566cb)


## Tech requirement
- [Python] - Yêu cầu từ phiên bản python 3.x
+ [Pip] - Yêu cầu trình quản lý gói pip
* [wget] - Dùng để tải các tệp nén chứa hadoop và nifi 
  
## Phần 1: Thu Thập dữ liệu

Mục Đích: Thu thập dữ liệu bao gồm điểm kết thúc học phần, điểm thi đầu vào và các bài báo liên quan tới sinh viên về máy local

Các Website lấy dữ liệu:
- https://ktdbcl.actvn.edu.vn/khao-thi/to-chuc-thi/ket-qua-thi.html?fbclid=IwZXh0bgNhZW0CMTEAAR2xloZngUWT3Xl5d4u0YOxp5DoIwBuGqt9KfAPz9SzoNz4n_Wm1ZrNff5M_aem_hVtwlsu5g3iDwhepiyi9Lg
+ https://thi.tuyensinh247.com/danh-sach-trung-tuyen-hoc-vien-ky-thuat-mat-ma-nam-2021-c24a65727.html
- https://thi.tuyensinh247.com/danh-sach-trung-tuyen-nam-2022-hoc-vien-ky-thuat-mat-ma-c24a71677.html
* https://diemthi.tuyensinh247.com/danh-sach-trung-tuyen-dh-cd/hoc-vien-ky-thuat-mat-ma-KMA.html
 
Thư viện sử dụng: Request(Python), BeautifulSoup(Python)

Đầu vào:

![image](https://github.com/user-attachments/assets/57fdc2a7-8592-4e4f-acbc-57506fca6277)

Kết quả:

![image](https://github.com/user-attachments/assets/e756647f-b242-46ea-867d-14a1eb08706f)
![image](https://github.com/user-attachments/assets/0b495acb-17ab-4feb-b410-8ef5b47b3d98)

![image](https://github.com/user-attachments/assets/a1c0874e-da5d-4149-9f51-aaa17b97d2fa)

![image](https://github.com/user-attachments/assets/272eadc3-8bab-4770-8bb9-009ecc6cf598)



 ## Phần 2: Xây dựng data lake
### 2.1: Xây dựng data lake
Mục đích: Xây dựng data lake chứa các dữ liệu đã được thu thập về, nhằm mục đích cho các analyzic sau này.

Công nghệ sử dụng: Hadoop
### 2.2: Xây dựng các luồng data để đẩy/lấy dữ liệu lên data lake
Mục đích: Xây dựng các luồng dữ liệu đẩy tự động từ máy local lên data lake để lưu trữ. Và xây dựng các luồng dữ liệu tự động lấy dữ liệu từ máy data lake về máy local nhằm mục đích phân tích dữ liệu.

Công nghệ sử dụng: Apache Nifi 



  
## Phần 3: Xử lý và trực quan hóa dữ liệu
Mục đích: Tận dụng những dữ liệu thô(dạng PDF) đã có trong hồ dữ liệu chuyển đổi, xử lý một số dữ liệu bị missing thành các file dữ liệu .CSV hữu ích. Sử dụng Python để trực quan hóa các file .CSV thành các biểu đổ phổ điểm nhằm tìm ra các hướng giải dạy thích hợp cho từng môn học.

Công cụ và thư viện sử dụng: pandas, numpy, matplotlib, fitz

Đầu vào các 

