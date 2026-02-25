"""
==================================================
A. INHERITANCE (Pewarisan)
==================================================
"""


class Produk:
    def __init__(self, nama_produk: str, harga: str):
        """
        Harga menggunakan str
        """
        self.__nama_produk = nama_produk
        self.__harga = harga

    def info_produk(self):
        return f"{self.__nama_produk}, Seharga: {self.__harga}"


class ProdukElektronik(Produk):
    def __init__(self, nama_produk: str, harga: str, garansi: int):
        self.__garansi = garansi
        super().__init__(nama_produk, harga)

    def info_produk(self):
        return f"{super().info_produk()}, dengan garansi {self.__garansi} tahun"


class ProdukMakanan(Produk):
    def __init__(self, nama_produk: str, harga: str, tanggal_kadaluarsa: str):
        self.__tanggal_kadaluarsa = str(tanggal_kadaluarsa)
        super().__init__(nama_produk, harga)

    def info_produk(self):
        return f"{super().info_produk()}, kadaluarsa {self.__tanggal_kadaluarsa}"


Elektro = ProdukElektronik("TV", "3.000.000", 2)
Makanan = ProdukMakanan("Roti", "15.000", "12-12-2026")

print(Elektro.info_produk())
print(Makanan.info_produk())

"""
==================================================
B. POLYMORPHISM
==================================================
"""


class Notifikasi:
    def __init__(self):
        self.__pesan = "Mengirim notifikasi melalui "

    def kirim(self):
        return f"{self.__pesan}"


class Email(Notifikasi):
    def __init__(self):
        self.__email = "Email"
        super().__init__()

    def kirim(self):
        return f"{super().kirim()}{self.__email}"


class SMS(Notifikasi):
    def __init__(self):
        self.__sms = "SMS"
        super().__init__()

    def kirim(self):
        return f"{super().kirim()}{self.__sms}"


Email = Email()
SMS = SMS()

print(Email.kirim())
print(SMS.kirim())

"""
==================================================
C. ENCAPSULATION
==================================================
"""


class Mahasiswa:
    def __init__(self):
        self.__nilai = "Nilai belum diset"

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai_baru: int):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            print("Nilai tidak valid")


Budi = Mahasiswa()
Andi = Mahasiswa()

Budi.set_nilai(100)
Andi.set_nilai(99)

print(Budi.get_nilai())
print(Andi.get_nilai())
