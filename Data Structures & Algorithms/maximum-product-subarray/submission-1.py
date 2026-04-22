class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return nums[0]
        dp = [[False] * n for i in range(n)]

        product = 0

        for i in range(n):
            dp[i][i] = nums[i]
            if dp[i][i] > product:
                product = dp[i][i]

        for length in range(2, n+1):
            for i in range(n-length+1):
                j= i+length-1
                if length == 2:
                    dp[i][j] = nums[i] * nums[j]
                else:
                    dp[i][j] = dp[i][j-1] * nums[j]

                if dp[i][j] > product:
                    product = dp[i][j]
        return product
        