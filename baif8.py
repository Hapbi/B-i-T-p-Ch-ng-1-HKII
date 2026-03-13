#Bài 8
class Student:
    def __init__(self, name, points):
        if 0 <= points <= 10:
            self.name = name
            self.points = points
        else:
            raise ValueError("Điểm phải từ 0 đến 10")
    def thongtin(self):
        print(f"Tên: {self.name}, điểm: {self.points}")
hocsinh = Student("Bốp", 11)
hocsinh2 = Student("An", 9.5)
