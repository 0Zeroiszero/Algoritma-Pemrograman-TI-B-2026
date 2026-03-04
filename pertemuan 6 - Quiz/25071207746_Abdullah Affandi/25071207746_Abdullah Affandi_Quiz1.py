# Bagian pertama
# Menampilkan daftar film
"""
SOAL 1
"""

daftar_film = [
    ["Danur", 50000],
    ["Inside Out", 45000],
    ["Interstellar", 55000],
    ["True Detective", 40000],
    ["Breaking Bad", 60000],
]

total_film = len(daftar_film)

print(f"Berikut daftar film yang tersedia (Total Film: {total_film})")

for i in range(len(daftar_film)):
    print(f"{i + 1}. {daftar_film[i][0]}")

print("\nTekan 0 untuk keluar")

"""
SOAL 2 mengembangkan kode SOAL 1
"""
pembelian_tiket = []
tiket_seluruh_hari = 0

while True:
    pembelian_tiket_judul_film = int(input("Pilih nomor film: "))
    if pembelian_tiket_judul_film == 0:
        break

    try:
        pilihan_film_dari_user = pembelian_tiket_judul_film
        if pilihan_film_dari_user > total_film:
            print("Nomor film tidak valid")
            break
    except ValueError:
        print("Nomor film tidak valid")
        break

    pembelian_tiket_total = int(input("Masukkan total tiket: "))
    if pembelian_tiket_total == 0:
        break

    tiket_seluruh_hari += pembelian_tiket_total

    pembelian_tiket.append(
        [
            f"{daftar_film[pembelian_tiket_judul_film - 1][0]}",
            f"{int(daftar_film[pembelian_tiket_judul_film - 1][1]) * pembelian_tiket_total}",
        ]
    )

    print()

# hasil kalkulasi di sum
pembelian_tiket_total_terkalkulasi = []
for i in pembelian_tiket:
    pembelian_tiket_total_terkalkulasi.append(int(i[1]))

print("== PILIHAN KAMU ===")
for v in pembelian_tiket:
    v_i = 1
    print(f"{v_i}. {v[0]}")
    v_i += 1

print(f"Total biaya: Rp{sum(pembelian_tiket_total_terkalkulasi)}\n")
"""
SOAL 3
"""
pembayaran_pengguna = int(input("Bayarlah sesuai dengan harga: "))
while pembayaran_pengguna < sum(pembelian_tiket_total_terkalkulasi):
    print("Jangan kurang duitnya\n")
    pembayaran_pengguna = int(input("Bayarlah sesuai dengan harga: "))

print(f"Kamu membayar dengan: Rp{pembayaran_pengguna}\n")

if pembayaran_pengguna > sum(pembelian_tiket_total_terkalkulasi):
    kembalian_pembayaran_pengguna = pembayaran_pengguna - sum(
        pembelian_tiket_total_terkalkulasi
    )
    print(f"Kembalian Anda: Rp{kembalian_pembayaran_pengguna}\n")
elif pembayaran_pengguna == sum(pembelian_tiket_total_terkalkulasi):
    print("Uang pas, tidak ada kembalian\n")

"""
SOAL 4
"""
print("== RECAP HARIAN ===")
"""
sehari mentotalkan seluruh tiket

[ <- ini non-index
    [Danur, 50000], <- ini indeks 0 ini per film hari ke-1
    [Danur, 50000], <- ini per film hari ke-2
]

pakai slice, dihitung ke bawah, dimulai dari hari ke-2 maka hari ke-2, dst.
hari ke-1 gak dianggap

matriks Nx2 dengan N tak hingga
sesuai permintaan dibuat dengan menghitung baris atau kolom dan bukan input
"""
hari_recap = int(input("Hari ke-"))

print(f"total tiket terjual per hari: {tiket_seluruh_hari}")

while len(pembelian_tiket[hari_recap - 1 :]) == 0:
    hari_recap = int(input(f"Gak ada hari ke-{hari_recap}: "))

print(f"total tiket terjual per film: {len(pembelian_tiket[hari_recap - 1 :])}")
