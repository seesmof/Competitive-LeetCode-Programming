import random


def binarySearch(arr, target):
    min, max = 0, len(arr) - 1

    while min <= max:
        mid = (min + max) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            max = mid - 1
        else:
            min = mid + 1
    return -1


names = []

for i in range(1000000):
    firstNames = [
        "Louise",
        "Russell",
        "Todd",
        "Jorge",
        "Stephen",
        "Ronald",
        "Albert",
        "Gordon",
        "Ina",
        "Mittie",
        "Tony",
        "Sarah",
        "Sylvia",
        "John",
        "Dylan",
        "Margaret",
        "Christine",
        "Ann",
        "Alfred",
        "Maud",
        "Margaret",
        "Estella",
        "Katie",
        "Claudia",
        "Dustin",
        "Grace",
        "Russell",
        "Georgia",
        "Zachary",
        "Vincent",
        "Mina",
    ]
    lastNames = [
        "Cole",
        "Peters",
        "Marshall",
        "Klein",
        "Davidson",
        "Frank",
        "Sherman",
        "Jimenez",
        "Salazar",
        "Schwartz",
        "Hoffman",
        "Castillo",
        "Russell",
        "Daniel",
        "Arnold",
        "Mann",
        "Jones",
        "Rowe",
        "Barrett",
        "Mullins",
        "Watson",
        "Gardner",
        "Chapman",
        "Curry",
        "Fernandez",
        "Dixon",
        "Mann",
        "Wood",
        "Walters",
        "Park",
        "Dixon",
    ]

    firstName = random.choice(firstNames)
    lastName = random.choice(lastNames)
    names.append(firstName + " " + lastName)

target = random.choice(names)


def dumbSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


import time

print()

dumbSearchResults = []
dumbSearchResult = 0
for i in range(10):
    startTime = time.time()
    result = dumbSearch(sorted(names), target)
    endTime = time.time()
    elapsedTime = (endTime - startTime) * 1000
    dumbSearchResults.append(elapsedTime)
for num in dumbSearchResults:
    dumbSearchResult += num
dumbSearchResult //= len(dumbSearchResults)

print(f"\nDUMB SEARCH\n")
print(f"Result: {result}")
print(f"Elapsed Time: {dumbSearchResult:.2f} milliseconds")

binarySearchResults = []
binarySearchResult = 0
for i in range(10):
    startTime = time.time()
    result = dumbSearch(sorted(names), target)
    endTime = time.time()
    elapsedTime = (endTime - startTime) * 1000
    binarySearchResults.append(elapsedTime)
for num in binarySearchResults:
    binarySearchResult += num
binarySearchResult //= len(binarySearchResults)

print(f"\nBINARY SEARCH\n")
print(f"Result: {result}")
print(f"Elapsed Time: {binarySearchResult:.2f} milliseconds")

print()
