"""
CONDITION:
While picking up Lalo's bail, Saul and Mike got lost in a desert. In a desert, they found a cactus: a connected undirected graph on n nodes, such that every edge in it appears in at most one simple cycle.

It turned out that n is even. For some reason, Mike and Saul want to solve the following problem:

Define d(u,v) as the shortest distance between nodes u and v in this cactus. Partition all n nodes into n/2 pairs (ui, vi), such that every node appears in exactly one pair, and the sum of d(ui, vi) is maximized.

What's the maximum possible sum of d(ui, vi) in such a partition?

INPUT:
The first line contains a single integer t - the number of test cases.

The first line of each test case contains two integers n,m - the number of nodes and edges correspondingly.

The i-th of the next m lines contains two integers ui, vi - denoting an edge between nodes ui and vi. It's guaranteed that these edges form a cactus.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10**5, and the sum of m over all test cases does not exceed 4⋅10**5

OUTPUT:
For each test case, output a single integer — the largest possible sum of d(ui, vi) in such a partition.

TEST CASES:
IN:
    3
    4 3
    1 2
    2 3
    3 4
    6 7
    1 2
    2 3
    3 1
    3 4
    4 5
    5 6
    6 4
    8 9
    1 2
    2 3
    3 1
    3 4
    4 5
    5 6
    6 7
    7 8
    8 3
OUT:
    4
    7
    11
"""

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
