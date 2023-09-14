n = int(input())
# print(f"{n//10} {n % 10}")
print()
seen = set()
for i in range(1, n+1):
    print(f"\n{i} and {n%i}\n")
    if n % i not in seen:
        seen.add(i)
print()
print(seen)
print(len(seen))
