Buổi 05 (22/10/2026)
# FastAPI - JWT

### Cài package cần thiết
```
pip install "fastapi[standard]" sqlmodel sqlmodel
```

### Cài XAMPP cho có MySQL
- Có thể cài riêng từng cái MySQL, MySQL Workbench
- XAMPP:
    + Chọn lựa hệ điều hành: https://sourceforge.net/projects/xampp/files/
    + Windows ==> chọn version 8.2.12 ==> chọn Portable hoặc install, nhớ chọn version có VC16
        - xampp-portable-windows-x64-8.2.12-0-VS16.zip
        - xampp-windows-x64-8.2.12-0-VS16-installer.exe
    + Start XAMPP:
        - Mở xampp-control.exe
        - Start: Apache, MySQL.
            - Chú ý port nếu đụng port thì chọn "Config"
            - Chọn "apache (httpd.conf)" cho port HTTP -->
            - Chọn "apache (httpd-ssl.conf)" cho port HTTPS -->