# User function Template for python3
class Solution:
    def perfectSum(self, arr, n, sum):
        MOD = 10**9+7
        num = 0
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == sum:
                    num += 1
        return num % MOD
