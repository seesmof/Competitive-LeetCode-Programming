nums = [54, 61, 64, 51, 70, 50, 23, 94, 37, 36, 15, 57, 17, 66, 4]
arr = [num for num in nums if num >= 60]


arr = [
    {"id": 1, "name": "Lola Glover", "age": 31},
    {"id": 2, "name": "Brian Armstrong", "age": 24},
    {"id": 3, "name": "Amelia Nunez", "age": 26},
]
arr = [i for i in arr if i["id"] % 2 != 0]
print(arr)
