import os

FOLDER = "daftar-file"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)


# List file outputnya result = [(nama_file, size), ()]
def list_files():
    """Mengembalikan list of (nama_file, ukuran) dari folder"""
    try:
        files = [
            f
            for f in os.listdir(FOLDER)
            if f.endswith(".txt") and os.path.isfile(os.path.join(FOLDER, f))
        ]
    except:
        return []
    files.sort()
    result = []
    for f in files:
        path = os.path.join(FOLDER, f)
        try:
            size = os.path.getsize(path)
        except:
            size = 0
        result.append((f, size))
    return result


def show_files(files):
    if not files:
        print("Tidak ada file .txt ditemukan.")
        return False
    print("\nFile tersedia:")
    for i, (name, size) in enumerate(files, 1):
        print(f"[{i}] {name} ({size} bytes)")
    return True


def read_file():
    files = list_files()
    if not show_files(files):
        return
    try:
        pilih = int(input("Pilih file (nomor): "))
        if 1 <= pilih <= len(files):
            nama = files[pilih - 1][0]  # Memilih dari list [(nama_file, size), ()]
            path = os.path.join(FOLDER, nama)
            with open(path, "r", encoding="utf-8") as f:
                print(f"\n--- Isi {nama} ---")
                print(f.read())
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")
    except Exception as e:
        print(f"Error: {e}")


def write_file():
    files = list_files()
    if files:
        print("\nFile yang sudah ada:")
        for i, (nama, _) in enumerate(files, 1):
            print(f"[{i}] {nama}")
        print("[0] Buat file baru")
    else:
        print("Tidak ada file .txt. Buat file baru.")
    try:
        pilih = input("Pilih nomor (atau 0 untuk baru): ")
        if not pilih.isdigit():
            print("Input harus angka.")
            return
        pilih = int(pilih)
        if pilih == 0:
            nama_baru = input("Nama file baru (akhiri .txt): ").strip()
            if not nama_baru.endswith(".txt"):
                nama_baru += ".txt"
            nama = nama_baru
        elif 1 <= pilih <= len(files):
            nama = files[pilih - 1][0]  # Memilih dari list [(nama_file, size), ()]
        else:
            print("Nomor tidak valid.")
            return
        print("Masukkan isi teks (baris kosong untuk selesai):")
        baris = []
        while True:
            line = input()
            if line == "":
                break
            baris.append(line)
        isi = "\n".join(baris)
        path = os.path.join(FOLDER, nama)
        with open(path, "w", encoding="utf-8") as f:
            f.write(isi)
        print(f"File '{nama}' berhasil disimpan.")
    except Exception as e:
        print(f"Error: {e}")


def delete_file():
    files = list_files()
    if not show_files(files):
        return
    try:
        pilih = int(input("Pilih file yang akan dihapus (nomor): "))
        if 1 <= pilih <= len(files):
            nama = files[pilih - 1][0]  # Memilih dari list [(nama_file, size), ()]
            yakin = input(f"Hapus '{nama}'? (y/n): ").lower()
            if yakin == "y":
                path = os.path.join(FOLDER, nama)
                os.remove(path)
                print(f"File '{nama}' dihapus.")
            else:
                print("Dibatalkan.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")
    except Exception as e:
        print(f"Error: {e}")


def append_file():
    files = list_files()
    if not show_files(files):
        return
    try:
        pilih = int(input("Pilih file untuk ditambahi (nomor): "))
        if 1 <= pilih <= len(files):
            nama = files[pilih - 1][0]  # Memilih dari list [(nama_file, size), ()]
            path = os.path.join(FOLDER, nama)
            print(f"Menambahkan ke '{nama}' (baris kosong selesai):")
            baris = []
            while True:
                line = input()
                if line == "":
                    break
                baris.append(line)
            if baris:
                with open(path, "a", encoding="utf-8") as f:
                    f.write("\n" + "\n".join(baris))
            print("Teks berhasil ditambahkan.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")
    except Exception as e:
        print(f"Error: {e}")


def search_files():
    files = list_files()
    if not files:
        print("Tidak ada file .txt untuk dicari.")
        return
    kata = input("Masukkan kata kunci: ").strip()
    if not kata:
        print("Kata kunci kosong.")
        return
    ditemukan = []
    for nama, _ in files:
        if kata.lower() in nama.lower():
            ditemukan.append(nama)
    if ditemukan:
        print(f"\nKata '{kata}' ditemukan di nama file:")
        for f in ditemukan:
            print(f"- {f}")
    else:
        print(f"Tidak ada file yang namanya mengandung '{kata}'.")
