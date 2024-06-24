"""
CONDITION:

To get 99.1% pure product, everything in the lab has to be thoroughly cleaned daily. Right now, Jesse is going to clean a shelf with books.

The shelf consists of n places for books. There are some books placed on the shelf (possibly, none). If some place is empty, Jesse can clean it without any power consumption (he is really good at cleaning). He cannot clean any place with a book currently in it. If there is a book at some place, and the adjacent place is empty, Jesse can move the book to that adjacent place consuming 1 power.

Jesse is a very busy person, and he does not want to spend too much power. For each test case, tell the minimal amount of power Jesse has to spend.

INPUT:

The first line of input contains a single integer t — the number of test cases.

The first line of each of the t test cases contains a single integer n - the number of the places on the shelf.

The second line contains a string s of length n, where si=0 if there is no book at i-th place, and si=1 otherwise.

It is guaranteed that in all provided test cases it is possible to clean the shelf.

The sum of n over all test cases will not be greater than 2⋅10**5.

OUTPUT:
Output t lines, each line containing a single integer — the minimal amount of power Jesse has to spend.

TEST CASES:
IN:
    3
    2
    01
    5
    00110
    9
    101010101
OUT:
    1
    2
    6

NOTE:
In the first test case, Jesse can do the following:

- Clean the first place;
- Move the book from the second place to the first (consuming 1 power);
- Clean the second place.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
