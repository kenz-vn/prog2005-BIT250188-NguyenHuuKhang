def tinh_diem_trung_binh():
    n = int(input("Nhập số lượng môn: "))
    tong = 0

    for i in range(n):
        diem = float(input(f"Nhập điểm môn {i+1}: "))
        tong += diem

    dtb = tong / n
    print(f"Điểm trung bình là: {dtb:.2f}")

tinh_diem_trung_binh()