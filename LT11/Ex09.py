def input_matrix(rows, cols, name):
    matrix = []
    print(f"\nNhập ma trận {name}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = input(f"Phần tử [{i}][{j}]: ")

            if val.strip() == "":
                print("Lỗi: Không được nhập giá trị trống!")
                return None
            row.append(float(val))
        matrix.append(row)
    return matrix
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))
A = input_matrix(rows, cols, "A")
if A is None:
    exit()
B = input_matrix(rows, cols, "B")
if B is None:
    exit()
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("\nMa trận tổng:")
for r in C:
    print(r)