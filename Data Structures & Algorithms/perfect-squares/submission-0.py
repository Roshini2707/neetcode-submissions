class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        for i in range(1, int(n ** 0.5) + 1):
            squares.append(i * i)

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break

                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]