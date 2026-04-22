class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n+1):
            one = 0
            for i in range(32):
                if (1 << i) & num:
                    one += 1
            output.append(one)
        return output

        