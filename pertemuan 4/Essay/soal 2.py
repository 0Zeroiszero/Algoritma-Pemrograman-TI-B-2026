try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")
except ValueError:
    print("Error: Masukkan hanya angka!")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")