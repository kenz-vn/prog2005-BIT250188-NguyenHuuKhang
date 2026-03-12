file = "product.txt"

code = input("Code: ")
name = input("Name: ")
price = float(input("Price: "))

with open(file, "a", encoding="utf-8") as f:
    f.write(f"{code};{name};{price}\n")

products = []
with open(file, "r", encoding="utf-8") as f:
    for line in f:
        c, n, p = line.strip().split(";")
        products.append((c, n, float(p)))

print("Danh sách sản phẩm:")
for p in products:
    print(p)

products.sort(key=lambda x: x[2], reverse=True)

print("Sản phẩm theo giá giảm dần:")
for p in products:
    print(p)