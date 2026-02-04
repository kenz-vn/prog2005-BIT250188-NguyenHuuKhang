for i in range(1, 4):
    print(f"\nNhap thong tin sinh vien {i}:")
    name = input("Ten: ")
    toan = float(input("Diem Toan: "))
    ly = float(input("Diem Ly: "))
    hoa = float(input("Diem Hoa: "))

    avg = (toan + ly + hoa) / 3

    print(f"Sinh vien: {name}")
    print(f"Diem trung binh: {avg:.2f}")