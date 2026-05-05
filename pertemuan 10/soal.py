"""
Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:


Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan dua algoritma pengurutan, yaitu dan , secara terpisah.
Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.

* Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
* Implementasikan fungsi terpisah untuk Radix Sort dan Merge Sort.
* Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.
"""


# Implementasi fungsi Radix Sort
def radixSort(arr):
    mylist = arr.copy()
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(mylist)
    exp = 1
    while maxVal // exp > 0:
        while len(mylist) > 0:
            val = mylist.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                mylist.append(val)

        exp *= 10

    return mylist


# implementasi fungsi Merge Sort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)


# implementasi fungsi menukar dua elemen dalam array
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    try:
        jumlah_elemen = int(input("Masukkan jumlah elemen (non-negatif): "))
        if jumlah_elemen <= 0:
            while jumlah_elemen <= 0:
                print("Jumlah elemen harus non-negatif.")
                jumlah_elemen = int(input("Masukkan jumlah elemen (non-negatif): "))
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat non-negatif.")
        jumlah_elemen = int(input("Masukkan jumlah elemen (non-negatif): "))

    elemen = []
    for i in range(jumlah_elemen):
        try:
            i_elemen = int(input(f"Masukkan elemen ke-{i + 1} (non-negatif): "))
            if i_elemen > 0:
                elemen.append(i_elemen)
            else:
                raise ValueError
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat non-negatif.")
            i_elemen = int(input(f"Masukkan elemen ke-{i + 1} (non-negatif): "))

    print("\nArray sebelum diurutkan:", elemen)
    print("Array setelah diurutkan (Radix Sort):", radixSort(elemen))
    print("Array setelah diurutkan (Merge Sort):", mergeSort(elemen))


if __name__ == "__main__":
    main()
