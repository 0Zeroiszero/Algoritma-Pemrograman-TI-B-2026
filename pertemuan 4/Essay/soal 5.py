try:
    data = input("Ketik sesuatu: ")
    angka = int(data)
    print(f"Anda memasukkan angka: {angka}")
except ValueError:
    print("Input bukan angka.")
finally:
    print("Program selesai dijalankan.")
