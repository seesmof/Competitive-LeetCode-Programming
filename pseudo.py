def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]


arr = [31, 22, 15, 18, 26, 51, 92]
print(arr)
selectionSort(arr)
print(arr)
