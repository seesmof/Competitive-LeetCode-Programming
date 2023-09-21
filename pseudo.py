debts = {}
debts["John"] = 35
debts["Alice"] = 51
debts["Clurk"] = 32

print(f"\n{debts}\n")

print(f'"Clurk" owes ${debts["Clurk"]}')
print(f'Is "Loki" in debt? {"Loki" in debts}')

print(f'\n"Clurk" paid out his debt, but "Loki" now owes $61')
del debts["Clurk"]
debts["Loki"] = 61

print(f"\nPeople in debt:", end=" ")
for person in debts:
    print(f"{person}", end=", " if person is not list(debts)[-1] else "")

print(f"\nAll debts:", end=" ")
for debt in debts.values():
    print(debt, end=", " if debt is not list(debts.values())[-1] else "")

print(f"\n\nAll people and their debts:")
for person, debt in debts.items():
    print(f"- {person} owers {debt}")

print()
print(debts.keys(), debts.values(), debts.items())
print()
print(debts.get("Loki"))
print(debts.get("Koki", "Nope"))

archive = dict({debt for debt in debts.items() if debt[1] < 60})
print(archive)
archive["Anne"] = 52
archive["Austin"] = 21

general = {debts, archive}
print(general)
