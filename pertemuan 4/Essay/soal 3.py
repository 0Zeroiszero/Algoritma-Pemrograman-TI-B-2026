buah = ["Apel", "Jeruk", "Mangga"]
try:
    index = int(input(f"Pilih index (0-{len(buah)-1}): "))
    print(f"Buah yang dipilih: {buah[index]}")
except ValueError:
    print("Error: Index harus berupa angka!")
except IndexError:
    print("Error: Index tidak ada dalam list!")