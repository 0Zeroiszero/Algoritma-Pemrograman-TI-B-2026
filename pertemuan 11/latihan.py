def linearSearch(arr, targetVal):
    for i, val in enumerate(arr):
        if val == targetVal:
            return i
    return -1


def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        elif arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def printResult(method, targetVal, result, dataset):
    print(f"\n{method}: mencari {targetVal} di {dataset}")
    if result != -1:
        print(f"  Ditemukan di index {result}")
    else:
        print("  Tidak ditemukan (-1)")


data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
dataSorted = sorted(data)

print(f"Data         : {data}")
print(f"Data (sorted): {dataSorted}")

targetVal = int(input("Masukkan nilai yang dicari: "))

linearResult = linearSearch(data, targetVal)
binaryResult = binarySearch(dataSorted, targetVal)

printResult("Linear Search", targetVal, linearResult, "data asli")
printResult("Binary Search", targetVal, binaryResult, "data yang sudah diurutkan")
