class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                subset = res[i]
                res.append(subset + [num])
        return res

        