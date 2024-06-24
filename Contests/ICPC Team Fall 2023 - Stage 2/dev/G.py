"""
CONDITION:
Gus is given a binary string s. He has to perform the following operation exactly once:

- Choose some subsequence of the string. Then, arrange characters on those positions in the sorted order.

For example, for string 011010110 Gus can choose symbols at positions 3,4,6,7,9 (underlined). Symbols at these positions form string 10010. After sorting them, Gus will get the string 010010111.

Gus wants to find the number of possible strings he might get after applying this operation exactly once. For him this problem is trivial, but can you solve it?

As this number can be very large, output it modulo 998244353.

INPUT:
The first line contains a single integer t - the number of test cases. The description of test cases follow.

The only line of each test case contains a binary string s.

It is guaranteed that the sum of lengths of s over all test cases does not exceed 10**6

OUTPUT:
For each test case, output a single integer  — the number of possible strings Gus might get after applying this operation exactly once.

TEST CASES:
IN:
    6
    0
    1
    01
    10
    1010
    0101010111001010100101011100101001010
OUT:
    1
    1
    1
    2
    4
    437686

NOTE:
For the fourth test case, the string is 10. If he selects both positions, he will get string 01. For any other selection, the string will remain 10. So, there are two possible strings he might obtain.

For the fifth test case, here are all possible strings: 1010, 0011, 0110, 1001.
"""

t = int(input())
for _ in range(t):
    s = input()
