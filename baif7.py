#Bài 7
class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points
hocsinh1 = Student("An Sinh Viên", 10)
hocsinh2 = Student("Bốp Sinh Viên", 9.5)
print("Tên:",hocsinh1.name, "//điểm:", hocsinh1.points)
print("Tên:",hocsinh2.name, "//điểm:", hocsinh2.points)
