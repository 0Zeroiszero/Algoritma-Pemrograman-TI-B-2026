data = [
    918,
    336,
    637,
    814,
    507,
    685,
    854,
    933,
    970,
    461,
    26,
    884,
    684,
    47,
    922,
    246,
    431,
    985,
    412,
    679,
    708,
    354,
    369,
    396,
    406,
    882,
    119,
    682,
    378,
    578,
    208,
    899,
    344,
    436,
    153,
    835,
    836,
    985,
    117,
    619,
    225,
    345,
    210,
    606,
    313,
    998,
    681,
    989,
    212,
    163,
    762,
    389,
    906,
    423,
    204,
    627,
    430,
    568,
    430,
    71,
    429,
    492,
    817,
    577,
    621,
    914,
    500,
    783,
    872,
    992,
    498,
    477,
    34,
    570,
    113,
    2,
    58,
    844,
    464,
    293,
    302,
    183,
    711,
    777,
    71,
    441,
    261,
    713,
    544,
    528,
    759,
    193,
    163,
    272,
    389,
    979,
    608,
    977,
    721,
    508,
    619,
    875,
    948,
    750,
    991,
    711,
    855,
    111,
    555,
    608,
    535,
    603,
    538,
    753,
    190,
    441,
    85,
    200,
    193,
    577,
    774,
    578,
    405,
    306,
    256,
    926,
    433,
    444,
    459,
    368,
    187,
    671,
    701,
    714,
    411,
    940,
    603,
    736,
    665,
    947,
    517,
    19,
    365,
    165,
    514,
    133,
    491,
    642,
    636,
    957,
]

print("===BUBBLE SORT===")


def bubble_sort(data: list):
    count_b = 0
    data1 = data.copy()

    n = len(data1)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data1[j] > data1[j + 1]:
                data1[j], data1[j + 1] = data1[j + 1], data1[j]
                count_b += 1
    return data1, count_b


counter_bubble = bubble_sort(data)
print(counter_bubble[0])
print(f"Jumlah swap bubble sort: {counter_bubble[1]}")


def selection_sort(data: list):
    count_s = 0
    data1 = data.copy()

    n = len(data1)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data1[j] > data1[min_index]:
                min_index = j
                count_s += 1

        min_value = data1.pop(min_index)
        data1.insert(i, min_value)

    return data1, count_s


counter_select = selection_sort(data)
print()
print("===SELECTION SORT===")
print(counter_select[0])
print(f"Jumlah swap selection sort: {counter_select[1]}")
