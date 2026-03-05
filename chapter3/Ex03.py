colors = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    colors.remove("Green")
except ValueError:
    print("Không có Green trong danh sách")

print(colors)