def jumlah_digit(n):
    if n < 10:
        return n
    return n % 10 + jumlah_digit(n // 10)

# Panggil fungsi untuk n = 1234
hasil = jumlah_digit(1234)
print(hasil)