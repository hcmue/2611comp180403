# Phân biệt List [] vs Dict {}, Tuple () vs Set ()

- List, Set, Tuple: Theo chỉ số index

  - Đánh từ 0 -> n-1, hoặc -n ===> -1
  - Set: Các phần tử ko trùng nhau
  - List vs Tuple: Tuple không thay đổi giá trị

- Dict: Truy xuất theo key
  - Truy xuất nhanh theo key
  - mydict["key"] ==> nếu key không có thì Error
  - mydict.get("key", default_value)

Btap: Cho mảng/danh sách điểm thi đại học của ngành Tin học. Hãy định điểm chuẩn, biết rằng ngành lấy X chỉ tiêu, lấy tối đa 120% chỉ tiêu
Gợi ý:
Bước 1: Thống kê
0 - 0.25: ? TS
0.26 - 0.50: ? TS
...
{
0: x,
0.25: y,
0.5: z
}
dễ hơn:
{
0: x, 1: x, 2, ..., 30: z
}

```
for i in range(mang)
```
