def digitalroot(n):
    return n if n < 10 else digitalroot(sum(int(digit) for digit in str(n)))


n = int(input())
print(digitalroot(n))
