DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

# ==== BAGIAN A ====


def tebak_angka(angka_rahasia: int, maks_percobaan: int):
    """Menebak angka dengan membandingkan angka rahasia dan
    dibatasi dengan maksimal percobaan"""
    coba = 0
    balik = [False, 0]
    while coba <= maks_percobaan:
        try:
            tebakan = int(input("Tebak angka: "))
            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            elif tebakan == angka_rahasia:
                print("Benar!")
                balik = [True, maks_percobaan - coba]
                return balik

            coba += 1

        except ValueError:
            print("Tidak Valid")
            tebakan = int(input("Tebak angka: "))
    print(f"Gagal, angkanya adalah {angka_rahasia}")
    return balik


def hitung_skor(berhasil: bool, sisa_percobaan: int):
    """Fungsi menghitung skor, return None jika error"""
    try:
        if berhasil:
            return sisa_percobaan
        else:
            return int(0)

    except ValueError:
        return


def main_satu_ronde(nama: str, nomor_ronde: int):
    """Memainkan satu ronde saja. Return list berisi [nama, skor], None jika error"""
    try:
        angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
        tebakan, sisa = tebak_angka(angka_rahasia, 10)
        skor = 0
        if tebakan:
            skor = hitung_skor(True, sisa)
        else:
            skor = hitung_skor(False, sisa)

        return [nama, skor]
    except ValueError:
        return


# ==== BAGIAN B ====


def tampilkan_riwayat(riwayat: list):
    """Menampilkan riwayat. return riwayat jika berisi atau KALIMAT Belum ada riwayat: jika kosong. None jika err"""
    try:
        if riwayat:
            return riwayat
        else:
            return "Belum ada riwayat"
    except ValueError:
        return


# ==== BAGIAN C ====


def selection_sort_riwayat(riwayat: list):
    "Melakukan sorting dari skor terbesar menggunakan matriks 2D [ [] ]"
    try:
        a = riwayat.copy()
        n = len(a)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if a[min_index][1] < a[j][1]:
                    min_index = j
                    a[min_index], a[i] = a[i], a[min_index]

        return a
    except IndexError:
        print("idx err")


def tampilkan_leaderboard(riwayat: list):
    """Menampilkan leaderboard loh ya"""
    try:
        a = selection_sort_riwayat(riwayat=riwayat)
        print("=== LEADERBOARD LOH YA ====")
        print("No  |        Nama        |   Skor   |")
        for i, v in enumerate(a):
            if i == 0:
                print(f"{i + 1}   |        {v[0]}        |   {v[1]}   |**")
            else:
                print(f"{i + 1}   |        {v[0]}        |   {v[1]}   |")
    except SyntaxError:
        print("Syntax Err")


# === PROGRAM UTAMA ===
riwayat = list()
ronde = 0


def back():
    global ronde
    nama = input("Masukkan nama lo: ")
    nama_s, skor = main_satu_ronde(nama, ronde)
    if nama_s:
        riwayat.append([nama_s, skor])
    ronde += 1

    lagi = input("Main lagi? Y/n: ")
    if lagi.lower() == "y":
        return back()
    else:
        return False


while True:
    lagi = back()
    if not lagi:
        tampilkan_riwayat(riwayat)
        print()
        tampilkan_leaderboard(riwayat)
        break
