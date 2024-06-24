"""
CONDITION:
Kim Wexler is tired of working for Mesa Verde. Instead, she wants to solve the following problem.

Kim has two integers a and b. Help her to find any x such that 0≤x≤10**9 and the value of (a+x) AND (b+x) is minimized.

Here AND denotes the bitwise AND operator.

INPUT:
The first line contains a single integer t — the number of test cases. Then t test cases follow.

The first line of each test case contains two space-separated integers a and b.

OUTPUT:
For each test case, output a single integer — the answer to the problem. If there are several integers x such that 0≤x≤10**9 and the value of (a+x) AND (b+x) is minimized, you can output any of them.

TEST CASES:
IN:
    2
    1 11
    64 64
OUT:
    1
    0

NOTE:
In the first test case, Kim can select x=1 to get (1+1) AND (11+1)=2 AND 12=0.

In the second test case, Kim can select x=0 to get (64+0) AND (64+0)=64 AND 64=64.
"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        print(1)

# FAILED
