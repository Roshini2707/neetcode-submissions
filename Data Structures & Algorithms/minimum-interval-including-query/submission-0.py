class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = []
        for i in queries:
            length = -1
            for start, end in intervals:
                if start <= i <= end:
                    if length == -1 or (end - start + 1) < length:
                        length = end - start + 1
            result.append(length)
        return result