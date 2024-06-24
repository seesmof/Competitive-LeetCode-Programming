"""
CONDITION:

When Mike Ehrmantraut started being a cop, he wanted all people to be equal before the law. Now he is retired, but he still wants all elements of an integer array a of length n to become equal.

He can perform the following operations:

1. Choose any i such that 1<=i<=n-1 and set ai=ai AND ai+1
2. Choose any i such that 2<=i<=n and set ai=ai AND ai-1

Find the smallest number of operations Mike needs to do to make all elements of a equal.

Here AND denotes the bitwise AND operation.

INPUT:

The first line of input contains a single integer t — the number of test cases.

The first line of each test case contains a single integer n - the length of the array.

The second line contains n integers a1,a2,...,an - the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10**5

OUTPUT:
For each test case, output a single integer — the answer to the problem.

TEST CASES:
IN:
    3
    2
    2 2
    5
    1 2 3 4 5
    4
    2 2 3 2
OUT:
    0
    5
    1

NOTE:
In the first test case, all numbers are already equal, so Mike doesn't need to do any operations.

In the second test case, it's enough to do the following 5 operations:

- Set a2 equal to a1 AND a2=1 AND 2=0.
- Set a1 equal to a1 AND a2=1 AND 0=0.
- Set a3 equal to a2 AND a3=0 AND 3=0.
- Set a4 equal to a3 AND a4=0 AND 4=0.
- Set a5 equal to a4 AND a5=0 AND 5=0.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
