"""
CONDITION:
Walter White finally broke bad and finished building his drug empire.

He has a network of n distributors, which looks like a tree. Jesse is the head distributor, numbered 0. For every i≥1, i-th distributor has a direct supervisor  — distributor pi with pi<i. Initially, distributor i has ai dollars.

Walter is going to shout for k times. Every time Walter shouts, the following will happen:

- For all 1≤i<n, i-th distributor will give all his money to its direct supervisor (all of them do this simultaneously).

After shouting k times, Walter will choose the distributor with the maximum amount of money and collect all his money.

For all k from 0 to n−1, find the amount of money Walter would collect after shouting exactly k times.

INPUT:

The first line of input contains a single integer t — the number of test cases.

The first line of each test case consists of a single integer n - the number of distributors.

The second line of each test case consists of n−1 integers p1,p2,...,pn−1 — where pi is a direct supervisor of distributor i. 

The third line of each test case consists of n integers a0,a1,...,an−1 — the initial amounts of money that distributors have. 

It is guaranteed that sum of n over all test cases does not exceed 2⋅10**5

OUTPUT:
For each test case print n integers  — the amount of money Walter would collect after shouting exactly k times, for all k from 0 to n−1.

TEST CASES:
IN:
    3
    4
    0 1 1
    1 3 4 2
    5
    0 1 2 1
    10 78 19 36 64
    6
    0 1 2 2 4
    25 29 27 20 23 28
OUT:
    4 6 10 10 
    78 88 171 207 207 
    29 54 81 124 152 152 

NOTE:
Consider the first test case.

- If Walt shouts 0 times, the amounts of money of distributors are (1,3,4,2). So, he will collect 4 dollars.
- If Walt shouts 1 time, the amounts of money of distributors are (4,6,0,0). So, he will collect 6 dollars.
- If Walt shouts 2 times, the amounts of money of distributors are (10,0,0,0). So, he will collect 10 dollars.
- If Walt shouts 3 times, the amounts of money of distributors are (10,0,0,0). So, he will collect 10 dollars.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
