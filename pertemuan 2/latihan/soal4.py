def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    return a * pangkat_rekursif(a, b - 1)

# Panggil fungsi untuk a = 2, b = 5
hasil = pangkat_rekursif(2, 5)
print(hasil)