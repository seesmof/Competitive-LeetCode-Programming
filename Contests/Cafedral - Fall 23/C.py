n = int(input())
res = 1
count = 2
for i in range(n):
    res += count
    count += 2
print(res)
