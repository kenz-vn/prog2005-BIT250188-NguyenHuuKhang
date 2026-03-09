def bai03():
    n = int(input("nhập n:"))
    print("hình 1:")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    print("hình 2:")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")