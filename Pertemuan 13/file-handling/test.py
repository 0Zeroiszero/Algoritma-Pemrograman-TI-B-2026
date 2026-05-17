from src import manager

def main():
    while True:
        print("\n" + "=" * 35)
        print("PYTHON FILE MANAGER v1.0")
        print("=" * 35)
        print("[1] Read file")
        print("[2] Write file")
        print("[3] Delete file")
        print("[4] Append file (bonus)")
        print("[5] Search (bonus)")
        print("[0] Exit")
        print("-" * 35)
        pilih = input("Pilih menu: ")
        if not pilih.isdigit():
            print("Menu tidak valid.")
            continue
        pilih = int(pilih)

        match pilih:
            case 0:
                print("Terima kasih.")
                break
            case 1:
                manager.read_file()
            case 2:
                manager.write_file()
            case 3:
                manager.delete_file()
            case 4:
                manager.append_file()
            case 5:
                manager.search_files()
            case _:
                print("Menu tidak valid.")


if __name__ == "__main__":
    main()
