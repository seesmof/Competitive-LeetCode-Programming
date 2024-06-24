"""
CONDITION:

Walter White has 2n students in his chemistry class. Student i has chemistry skill a 

He wants to divide students into n pairs for a group exercise. The pair works better together if their skills are closer. More precisely,

- If skills of students in a pair differ by more than A, they will blow up the lab;
- If skills of students in a pair differ by at most A, but by more than B, they will produce a mediocre product;
- If skills of students differ by at most B, they will produce 99.1% pure product.

Walter wants to split students into n pairs so that:

- Lab is not blown up;
- The number of pairs that produced 99.1% pure product is as large as possible.

Determine if Walter can split students in such a way, and if he can, find the largest possible number of pairs that would produce 99.1% pure product.

INPUT:

The first line of input contains a single integer t — the number of test cases.

The first line of each test case contains three integers n,A,B - the number of students.

The second line of each test case contains 2n integers a1,a2,...,a2n - skills of the students.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10**5

OUTPUT:
For each test case, if there is no way to split the students into pairs without blowing up the lab, output −1. Otherwise, output the largest possible number of pairs that would produce 99.1% pure product.

TEST CASES:
IN:
    4
    1 2 1
    42 69
    2 3 1
    1 2 3 4
    2 5 1
    6 1 3 4
    5 19 1
    1 7 8 9 10 11 12 13 14 20
OUT:
    -1
    2
    1
    4

NOTE:
In the first test case, it's impossible to split students into pairs without blowing up the lab.

In the second test case, we can pair the first student with the second, and the third one with the fourth one. Both pairs will have a difference in skills equal to 1, and both will produce 99.1% pure product.
"""

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    skills = list(map(int, input().split()))
