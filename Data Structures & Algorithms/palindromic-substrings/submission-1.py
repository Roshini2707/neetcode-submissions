class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n<=1:
            return 1
        dp = [[False] * n for i in range(n)]
        max_len = 1
        start = 0
        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1

        for length in range(2, n+1):
            for i in range(n-length+1):
                j= i+length-1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and length >= max_len:
                    max_len = length
                    start = i
                    count += 1
        return count       
        