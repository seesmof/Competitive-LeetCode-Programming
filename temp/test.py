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
