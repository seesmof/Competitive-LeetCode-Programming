"""
CONDITION:
Once Charles McGill prepared a problem for SEERC. It's input section looked like this:

The first line contains a single integer t (1≤t≤T) — the number of test cases.

The first line of each test case contains a single positive integer n.

⋮

It is guaranteed that the sum of n**2 over all test cases does not exceed K.

Chuck realized that he forgot to tell anything about the sum of n. What if it's too large and it might take too long to read the input?

Unfortunately, Chuck suffers from electromagnetic hypersensitivity, so he can't use his computer to check this. Help him: find the largest possible sum of n under the constraints from the statement.

INPUT:
The first line contains a single integer T — the number of test cases. Then T test cases follow.
The only line of each test case contains two space-separated integers T and K.

OUTPUT:
For each test case, output a single integer — the largest possible sum of n under the constraints of the problem.

TEST CASES:
IN:
    3
    4 30
    1 1000000000000000000
    69 42
OUT:
    10
    1000000000
    42

NOTE:
In the first test case, the largest possible sum is 10. One way to get it is when t=4 and corresponding values of n are 1,2,3,4: 1**2+2**2+3**2+4**2=30, 1+2+3+4=10. Another way to get it is with the following values of n: 2,2,3,3: 2**2+2**2+3**2+3**2=26<30, 2+2+3+3=10. 
"""

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    sum = 0
    i = 1
    while i**2 <= k:
        sum += i
        k -= i**2
        i += 1
    print(sum)

# FAILED
