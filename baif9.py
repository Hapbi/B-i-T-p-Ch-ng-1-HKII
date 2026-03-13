#Bài 9
class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def display(self):
        print(f"Tên: {self.name}, điểm: {self.points}")
hocsinh = Student("Bốp", 10)
hocsinh2 = Student("An", 9.5)
hocsinh.display()
hocsinh2.display()
