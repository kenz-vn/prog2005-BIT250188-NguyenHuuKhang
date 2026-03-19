class SinhVien:
    count = 0

    def __init__(self):
        SinhVien.count += 1

    @classmethod
    def dem(cls):
        return cls.count

sv1 = SinhVien()
sv2 = SinhVien()
print(SinhVien.dem())