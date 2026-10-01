import math
mang = [1.25, 13.5, 23.4, 29.5, 2.9, 2.67]
N = 5


# Thống kế
thong_ke = {}
for i in range(len(mang)):
    diem_lam_tron = math.ceil(mang[i])
    print(mang[i], diem_lam_tron)
    thong_ke[diem_lam_tron] = thong_ke.get(diem_lam_tron, 0) + 1

print(thong_ke)
xyz = list(reversed(sorted(thong_ke)))
print(xyz)