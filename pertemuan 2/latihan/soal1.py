def rata_rata(nilai):
    if not nilai:
        return "Data kosong"
    return sum(nilai) / len(nilai)


hasil = rata_rata([80, 75, 90, 60, 85])
print(hasil)
