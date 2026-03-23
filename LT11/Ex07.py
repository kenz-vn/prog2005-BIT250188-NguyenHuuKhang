import csv
name = input("Nhập tên nhân viên: ")
age = input("Nhập tuổi: ")
emp_id = input("Nhập ID: ")
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {name}\n")
    f.write(f"Tuổi: {age}\n")
    f.write(f"ID: {emp_id}\n")
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([name, age, emp_id])
print("Đã lưu file thành công!")