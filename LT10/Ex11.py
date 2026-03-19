while True:
    print("\n1. Bài 4")
    print("2. Bài 6")
    print("3. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        s = input("Nhập chuỗi: ")
        if s == "":
            print("Chuỗi rỗng!")
        else:
            print(len(s))

    elif choice == "2":
        s = input("Nhập chuỗi: ")
        rev = ""
        for c in s:
            rev = c + rev
        print(rev)

    elif choice == "3":
        break

    else:
        print("Chọn sai!")