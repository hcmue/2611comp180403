- Không khai báo kiểu dữ liệu (js, python, php)
  ==> Kiểu dữ liệu phụ thuộc giá trị.
- Ko kết thúc dòng bằng ;
- Đánh dấu khối lệnh bằng khoảng trắng (bằng nhau), ko có {}. Trước đánh dấu khối thường có dấu :

```
if x > 5:
    a = 7
    b = 6
```

- Cú pháp toán tử 3 ngôi (lệnh if đủ, có trả về giá trị)
  giá*trị_khi*đúng if biểu*thức*điều_kiện else giá_trị_khi_sai
  VD: x = "Âm" if a < 0 else "Không âm"

- hàm range:
  range(max): Từ 0, tăng 1, nhỏ hơn max
  range(start, max): Từ start, tăng 1, nhỏ hơn max
  range(start, max, step): Từ start, tăng step, nhỏ hơn max

- Chuỗi:
  Nháy đơn (') hoặc nháy kép (") để bao bọc chuỗi
  Nếu chuỗi nằm nhiều dòng thì dùng ''' .... ''' hoặc """ ... """
  Nếu trong chuỗi nếu có nếu biến và f'' ở đầu thì sẽ bị thay thế

- Về nhà:

* Phân biệt List [] vs Dict {}, List [] vs Set ()
* Tạo môi trường ảo https://www.hcmue.io.vn/courses/comp1804/notes
  1. Tạo python -m venv <ten_thu_muc>
  2. Activate môn trường: <ten_thu_muc>\Scripts\activate
  3. Cài thêm thư viện: pip install <ten_thu_vien>
  4. Export thư viện: pip freeze > requirements.txt
     5' Cài đặt môi trường project:
     pip install -r requirements.txt
