import json

with open("employees.json", "r") as file:
    data = json.load(file)

disease_count = {}
for employee in data["employees"]:
    if employee["disease"] not in disease_count:
        disease_count[employee["disease"]] = 0
    disease_count[employee["disease"]] += 1

for disease, count in sorted(disease_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{disease}: {count}")
