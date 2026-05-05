struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {"pendahuluan.docx": 45, "latar_belakang.docx": 62},
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {"paper_A.pdf": 340, "paper_B.pdf": 210},
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {"sistem.png": 430},
            },
        },
        "sidang": {"presentasi.pptx": 2048, "catatan_revisi.txt": 15},
        "README.txt": 8,
    }
}

aqil = struktur["Skripsi_Aqil"]


def total_ukuran(folder):
    total = 0
    for item in folder.values():
        if isinstance(item, dict):
            total += total_ukuran(item)
        else:
            total += item
    return total


def hitung_file(folder):
    count = 0
    for item in folder.values():
        if isinstance(item, dict):
            count += hitung_file(item)
        else:
            count += 1
    return count


def cari_terbesar(folder):
    terbesar_nama = None
    terbesar_size = 0

    for key, item in folder.items():
        if isinstance(item, dict):
            hasil = cari_terbesar(item)
            if isinstance(hasil, str) and ": " in hasil:
                parts = hasil.split(": ")
                size = int(parts[1])
                if size > terbesar_size:
                    terbesar_nama = parts[0]
                    terbesar_size = size
        else:
            if item > terbesar_size:
                terbesar_nama = key
                terbesar_size = item

    if terbesar_nama:
        return f"{terbesar_nama}: {terbesar_size}"
    return "0"


def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indent = "  " * level
    print(f"{indent}- 📁 {nama}")
    for key, value in folder.items():
        if isinstance(value, dict):
            tampilkan_tree(value, key, level + 1)
        else:
            print(f"{indent}  - 📄 {key} ({value} KB)")


print(f"Total ukuran skripsi: {total_ukuran(aqil)} KB")
print(f"Total jumlah file: {hitung_file(aqil)} file")
print(f"File terbesar: {cari_terbesar(aqil)} KB")
tampilkan_tree(aqil, "Skripsi_Aqil")
