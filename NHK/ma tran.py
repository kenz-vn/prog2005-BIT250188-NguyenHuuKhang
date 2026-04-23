matrix = [
    [100, 14, 8, 22, 71],
    [0, 243, 68, 1, 30],
    [90, 21, 7, 67, 112],
    [115, 200, 70, 150, 8]
]

for row in matrix:  # duyệt từng dòng
    for elem in row:  # Lấy từng phần tử trên mỗi dòng
        print('{:>4}'.format(elem), end='')
    print()