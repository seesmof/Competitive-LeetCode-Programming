def root(n):
    while n > 9:
        n = sum(int(x) for x in str(n))
    return n


n = int(input())
print(root(n))
