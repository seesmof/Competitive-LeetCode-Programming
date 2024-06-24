"""
CONDITION:
Albuquerque is a large city. It has n crossings and n−1 one-directional roads between them. It's guaranteed that if all roads were undirected, it would be possible to get from any crossing to any other by these roads. Additionally, every crossing has a label: S or F, indicating start and finish correspondingly.

- Choose any road (u,v) such that the following conditions hold:
    - This road is directed from crossing u to crossing v
    - Crossing u has label S
    - Crossing v has label F
- Change the direction of the road and swap labels on u and v.

What is the total number of different configurations that Saul and Kim can achieve by applying this operation any number of times? As this number can be very large, output it modulo 998244353.

Two configurations are called different if some crossing has different labels in them, or if some road has different orientation in them.

INPUT:
The first line of the input contains a single integer n - the number of crossings in Albuquerque.

The second line of the input contains a string of length n, consisting of characters S and F. The i-th character of this string denotes the initial label of crossing i.

The i-th of the next n−1 lines contains two integers ui, vi — denoting a directed road from crossing ui to crossing vi. It's guaranteed that if all roads were undirected, it would be possible to get from any crossing to any other by these roads.

OUTPUT:
Output a single integer  — the total number of different configurations that Saul and Kim can achieve by applying this operation any number of times, modulo 998244353.

TEST CASES:
IN:
    5
    SFSFS
    2 1
    2 3
    4 3
    4 5
OUT:
    1

IN:
    4
    SFFF
    1 2
    1 3
    1 4
OUT:
    4

IN:
    7
    SSSSFFF
    1 2
    3 2
    4 3
    4 5
    4 6
    2 7
OUT:
    13

NOTE:
In the first sample, all roads are directed from crossings with F on them to crossings with S on them, so it's impossible to do any operations.

In the second sample, for each v=2,3,4 it's possible to do an operation with nodes 1,v. Resulting three configurations, together with the initial one, are the only possible configurations.
"""

n = int(input())
s = input()
labels = []
for i in range(n - 1):
    u, v = map(int, input().split())
    labels.append((u, v))
