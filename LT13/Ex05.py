class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Tên: {self.name}, Màu: {self.color}"

f = Flower("Hoa hồng", "Đỏ")
print(f)