def isPalindrome(s):
    return s == s[::-1]


t = int(input())
for _ in range(t):
    s = input()
    if isPalindrome(s) is False:
        print("YES")
        print(s)
    elif isPalindrome(s) is True:
        if len(s) % 2 == 0:
            print("NO")
        else:
            print("YES")
            print("".join(sorted(s)))
