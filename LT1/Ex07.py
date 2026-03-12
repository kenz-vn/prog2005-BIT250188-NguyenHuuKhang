class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

sv1 = Student("Tâm", 8)
sv2 = Student("Khang", 9)

print(sv1.ten, sv1.diem)
print(sv2.ten, sv2.diem)