"""
CONDITION:

Jesse has a permutation p1,p2,...,pn of integers from 1 to n. His job is simple: to maximize the number of positions i, for which pi=i. To achieve that, Jesse 

- Color some elements of the permutation in yellow, and all the remaining elements in blue. There has to be at least one yellow and at least one blue element.
- Then, separately sort yellow and blue numbers.

For example, for permutation (3,5,1,6,2,4), Jesse can mark numbers 3,5,4 yellow, and 1,6,2 blue. After sorting yellow and blue elements separately, Jesse will get permutation (3,4,1,2,6,5).

Jesse's score in the end is the number of positions i, for which pi=i. Find the maximal score Jesse can achiev and some way to achieve it.

INPUT:
The first line contains a single integer t - the number of test cases.

The first line of each test case contains a single integer n (2≤n≤10**6) - the length of the permutation.

The second line of each test case contains n integers p1,p2,...,pn - elements of the permutation.

It is guaranteed that the sum of n over all test cases does not exceed 10 

OUTPUT:

For every test case, in the first line, output the maximal score Jesse can achieve.

In the second line, output a single integer k (1≤k≤n−1)  — the number of elements Jesse should color yellow.

In the third line, output k integers pos1,pos2,...,posk - the positions of the elements that you are going to color in yellow. 

If there are several ways to obtain the maximum score, output any of them.

TEST CASES:
IN:
    3
    2
    2 1
    4
    2 1 4 3
    6
    3 5 4 2 6 1
OUT:
    0
    1
    1 
    4
    2
    1 2 
    4
    3
    1 3 4 

NOTE:
In the first test case, for permutation (p1,p2)=(2,1), Jesse can mark p1 yellow and p2 blue. After sorting it will remain being (2,1), with score 0.

In the second test case, for permutation (p1,p2,p3,p4)=(2,1,4,3), Jesse can mark p1,p2 yellow and p3,p4 blue. After sorting the permutation will become (1,2,3,4), with score 4.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
