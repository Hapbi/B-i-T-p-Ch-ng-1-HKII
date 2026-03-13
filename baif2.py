#Bài 2
import math
a = float(input("nhap so: "))
b = float(input("nhap so: "))
#lữy thừa
luy_thua = a ** b
#chia lấy phần nguyên
nguyen = a // b
#chia lấy phần dư
du = a % b
#làm tròn số
lam_tron = round(a)
lam_tron2 = round(b)
print("đây là lũy thừa", luy_thua)
print("lấy phần nguyên", nguyen)
print("chia lấy phần dư", du)
print("làm tròn số", lam_tron,lam_tron2)
