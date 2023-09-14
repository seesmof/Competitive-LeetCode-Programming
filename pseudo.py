def isPalindrome(s):
    return s == s[::-1]


def findPalindrome(s):
    return s[::-1]


s = input()
t = findPalindrome(s)
print(t if isPalindrome(s+t) and isPalindrome(t+s) else -1)
