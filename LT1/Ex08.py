class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        if 0 <= diem <= 10:
            self.diem = diem
        else:
            raise ValueError("Điểm phải từ 0 đến 10")

sv1 = Student("Tâm", 8)
sv2 = Student("Khang", 9)

print(sv1.ten, sv1.diem)
print(sv2.ten, sv2.diem)