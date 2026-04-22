class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen ={}
        for i in nums:
            if i in seen:
                seen[i] += 1
                return True
            seen[i] = 1
        return False

        