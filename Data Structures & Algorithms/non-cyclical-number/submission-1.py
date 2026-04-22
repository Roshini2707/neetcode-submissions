class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False

    def sumOfSquares(self, n):
        result = 0
        while n:
            r = n % 10
            n = n // 10
            result += r * r
        return result

        