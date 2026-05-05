mylist = [170, 45, 75, 90, 802, 24, 2, 66]


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


print(radixSort(mylist))
