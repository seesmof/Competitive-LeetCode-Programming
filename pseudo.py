def countDifferentNumbers(n):
    seen = set()
    for i in range(1, n+1):
        see = n % i
        if see not in seen:
            seen.add(see)
    return len(seen)


n = int(input())
print(countDifferentNumbers(n))
