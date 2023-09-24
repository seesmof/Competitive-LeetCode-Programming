import json

with open("employees.json", "r") as file:
    data = json.load(file)

# Initialize an empty dictionary to hold the counts of each disease
disease_count = {}

# Iterate over all employees in the data
for employee in data["employees"]:
    # If the employee's disease is not already in the dictionary, add it with a count of 0
    if employee["disease"] not in disease_count:
        disease_count[employee["disease"]] = 0

    # Increment the count for the employee's disease
    disease_count[employee["disease"]] += 1

for disease, count in sorted(disease_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{disease}: {count}")

"""
Using range(len(arr)) in Python loops is not considered Pythonic for several reasons:

1. It is less readable: When you use range(len(arr)) it is not immediately clear that you're iterating over the elements of the array.

2. It is slower: Calling len(arr) is an O(1) operation in Python, but creating the list of indices up to len(arr) is an O(n) operation. For large lists, this is a significant overhead.

One viable alternative to using range(len(arr)) is to use enumerate(arr), which returns each element along with its index. This is typically what you want if you're using range(len(arr)).

Another alternative, if you don't need the index, is to directly use the list as your iterator (i.e., for element in arr). This is more Pythonic and faster.
"""
