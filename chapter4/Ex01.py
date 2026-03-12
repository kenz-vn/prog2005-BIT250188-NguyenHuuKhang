def thong_ke(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat

t = (3, 7, 1, 9, 5)
print(thong_ke(t))