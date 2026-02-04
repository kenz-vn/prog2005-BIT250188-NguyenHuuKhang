weight = float(input("Nhap can nang (kg): "))
height = float(input("Nhap chieu cao (m): "))

bmi = weight / (height * height)

print(f"BMI cua ban la: {bmi:.2f}")