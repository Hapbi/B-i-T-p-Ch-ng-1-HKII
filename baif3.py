#Bài 3
nhapdulieu = int(input("Nhập số từ 1 đến 9: "))
if 1 <= nhapdulieu <= 9:
    print(f"Bảng cửu chương của {nhapdulieu}")
    for i in range(1,10):
        print(f"{nhapdulieu} * {i} = {nhapdulieu * i}")
else:
    print("Số nhập phải là từ 1 đến 9: ")
