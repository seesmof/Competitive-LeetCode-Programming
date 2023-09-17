import random


def dumbSearch(items, item):
    for i in range(len(items)):
        if items[i] == item:
            return i
    return None


def binarySearch(items, item):
    low = 0
    high = len(items)-1

    while low <= high:
        mid = (low+high)
        guess = items[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


items = list(range(1000))
item = random.choice(items)
print(
    f"BIN. Searching for {item}. Result = {binarySearch(items, item)}")
print(f"DUM. Searching for {item}. Result = {dumbSearch(items, item)}")
