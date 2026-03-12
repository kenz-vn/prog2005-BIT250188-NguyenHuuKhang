data = {"a": 1, "b": 2, "c": 3}

key_can_kiem_tra = input("Nhập key cần kiểm tra: ")

if key_can_kiem_tra in data:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại")