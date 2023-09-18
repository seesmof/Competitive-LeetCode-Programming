import random

names = [
    "Isabel Tran",
    "John Glover",
    "Mollie Rodgers",
    "Julia Page",
    "Eula Green",
    "Hester Copeland",
    "Landon Castillo",
]
names = sorted(names)


def search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


guess = random.choice(names)
print(f"\nSearching for \"{guess}\" in {', '.join([f'{name}' for name in names])}\n")
result = search(names, guess)
if result != -1:
    print(f"Found at {result}")
else:
    print(f"Not found :(")
print()
