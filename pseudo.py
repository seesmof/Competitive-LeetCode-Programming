def binary(arr, pin):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        gues = arr[mid]

        if gues == pin:
            return mid
        if gues > pin:
            high = mid-1
        else:
            low = mid+1
    return -1
