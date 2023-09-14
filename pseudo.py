def countMinMillions(n, m, c):
    lenC = len(c)
    results = []
    for i in range(lenC):
        for j in range(i+1, lenC):
            results.append((c[i]+c[j]) % m)
    minResults = []
    print(f"\n{results}\n")
    for i in range(len(results)):
        if results[i] == 0:
            continue
        tmp = results[i]
        print(f"\n{tmp}\n")
        for j in range(i+1, len(results)):
            tmp += results[j]
            print(f"cur = {results[i]+results[j]}")
        print()
        minResults.append(tmp)
    print(minResults)
    return min(minResults)


n, m = input().split()
n, m = int(n), int(m)
c = [int(i) for i in input().split()]
print(countMinMillions(n, m, c))
