"""
CONDITION:
Help Walter solve his final problem.

For a positive integer n, define highest_bit(n) as the largest number i, such that 2**i<=n. Also define highest_bit(0)=-1 

You are given a positive integer X. Find the number of multisets S of positive integers, which satisfy the following conditions:

- All elements of S are nonnegative powers of 2.
- The sum of elements of S is X.
- There is no way to split elements of S into two groups so that highest_bit(S1)=highest_bit(S2), where S1 is the sum of the elements in the first group, and S2 is the sum of the elements in the second group.

Solve this problem for X=1,2,…,n.

Since the answers can be very large, output them modulo 998244353.

INPUT:
The only line of the input contains a single integer n.

OUTPUT:
Output n integers: answers to the problem for X=1,2,…,n, modulo 998244353.

TEST CASES:
IN:
    10
OUT:
    1 1 2 1 1 3 6 1 1 2 
"""

n = int(input())
