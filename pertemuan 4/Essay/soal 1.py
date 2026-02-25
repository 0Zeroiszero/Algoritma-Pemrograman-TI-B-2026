try:
    umur = int(input("Masukkan umur Anda: "))
    print(f"Umur Anda adalah {umur} tahun.")
except ValueError:
    print("Error: Input harus berupa angka!")
