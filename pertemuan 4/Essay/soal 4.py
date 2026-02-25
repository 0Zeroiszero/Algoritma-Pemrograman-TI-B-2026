try:
    nilai = int(input("Masukkan nilai ujian (0-100): "))
except ValueError:
    print("Error: Input harus angka!")
else:
    if 0 <= nilai <= 100:
        print("Nilai valid diterima.")
    else:
        print("Error: Nilai harus antara 0 sampai 100.")
