n = int(input("Nhập số người: "))
data = {}
for i in range(n):
    name = input(f"Nhập tên người {i+1}: ")
    age = int(input(f"Nhập tuổi người {i+1}: "))
    data[name] = age
avg_age = sum(data.values()) / len(data)
print("\nTuổi trung bình:", round(avg_age, 2))
items = list(data.items())
for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]
print("\nDanh sách sau khi sắp xếp:")
for name, age in items:
    print(name, ":", age)