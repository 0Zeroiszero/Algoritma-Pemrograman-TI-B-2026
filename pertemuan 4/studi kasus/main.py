import hashlib

class HashVerificationError(Exception):
    pass

def error(pesan):
    print(f"[ERROR] {pesan}")

def hitung_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        raise HashVerificationError("File tidak ditemukan!")

def main():
    try:
        path = input("Masukkan path file: ")
        expected_hash = input("Masukkan hash yang diharapkan: ")

        if not expected_hash.isalnum():
            raise ValueError("Format hash tidak valid!")

        actual_hash = hitung_hash(path)
        
        if actual_hash != expected_hash:
            raise HashVerificationError("Hash tidak cocok!")
            
        print("Verifikasi Berhasil: Integritas file terjaga.")
        
    except HashVerificationError as e:
        error(e)
    except ValueError as e:
        error(f"Input Error: {e}")
    except Exception as e:
        error(f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    main()

# path: pertemuan 4\studi kasus\Komikku-arm64-v8a-v1.13.5.apk
# hash sha256: 420bc78407b7f97dde7ae6982700b56a1f99c63c13e103f0f57ef4efba90e89b