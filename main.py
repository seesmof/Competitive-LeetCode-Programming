def recursiveFactorial(n):
    if n == 0:
        return 1
    return n * recursiveFactorial(n - 1)


print(recursiveFactorial(5))
