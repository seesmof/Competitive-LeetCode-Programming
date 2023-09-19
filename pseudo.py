def countDown(n):
    print(n)
    if n <= 1:
        return
    else:
        countDown(n - 1)


countDown(3)
