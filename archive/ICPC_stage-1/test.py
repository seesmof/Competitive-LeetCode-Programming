def isPalindrome(s):
    return s == s[::-1]


t = int(input())
for _ in range(t):
    s = input()
    if len(s) < 1:
        print("NO")
    elif isPalindrome(s) is False:
        print("YES")
        print(s)
    elif isPalindrome(s):
        print("YES")
        print("".join(sorted(s)))
