def lay_ten_file(path):
    return path.split("\\")[-1]

def lay_ten_bai_hat(path):
    file = path.split("\\")[-1]
    return file.split(".")[0]

path = r"d:\music\muabui.mp3"

print(lay_ten_file(path))
print(lay_ten_bai_hat(path))