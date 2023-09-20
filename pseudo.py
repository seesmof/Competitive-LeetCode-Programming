def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[n // 2]
    less = [el for el in arr if el < pivot]
    equal = [el for el in arr if el == pivot]
    more = [el for el in arr if el > pivot]

    return quickSort(less) + equal + quickSort(more)


arr = [
    32,
    15,
    7,
    90,
    42,
    18,
    63,
    51,
    24,
    8,
    60,
    82,
    11,
    37,
    45,
    5,
    74,
    28,
    95,
    69,
    2,
    56,
    79,
    23,
    61,
    17,
    3,
    88,
    70,
    48,
    36,
    1,
    55,
    9,
    71,
    33,
    91,
    14,
    67,
    29,
    77,
    6,
    47,
    13,
    85,
    19,
    68,
    41,
    21,
    86,
    46,
    25,
    38,
    4,
    72,
    64,
    30,
    57,
    22,
    31,
]

res = quickSort(arr)
print(res)
