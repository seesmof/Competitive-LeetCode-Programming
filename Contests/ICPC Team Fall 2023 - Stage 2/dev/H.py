"""
CONDITION:
Howard Hamlin likes to run. He decided that he is going to run for A consecutive minutes today.

Howard can run in two modes: slow and fast. The following conditions hold:

- Howard can run in fast mode for at most B minutes in a row;
- After Howard ran in a fast mode for some time, he has to rest for at least the same amount of time. More formally, if Howard ran for X minutes in a row in fast mode and switched to the slow mode, he won't be able to run in fast mode for at least X next minutes;
- Howard can only switch running modes at integer points in time.

Howard wants to run in fast mode as much as possible. What's the largest number of minutes out of all A minutes that Howard could spend running in a fast mode?

INPUT:
The first line contains a single integer T — the number of test cases. Then T test cases follow.
The only line of each test case contains two space-separated integers A and B.

OUTPUT:
For each test case, output a single integer  — the largest number of minutes out of all A minutes that Howard could spend running in a fast mode.

TEST CASES:
IN:
    4
    3 1
    10 10
    69 42
    5 1
    5 2
OUT:
    1
    5
    34
    3
    2

NOTE:
In the first test case, Howard can run for the first minute in the fast mode, then run for the second minute in the slow mode, and then run for the third minute in fast mode again.

In the second test case, Howard can run for all 10 minutes in the fast mode.
"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if b >= a // 2:
        print(a // 2)
    else:
        print((a + 1) // 2)

# FAILED
