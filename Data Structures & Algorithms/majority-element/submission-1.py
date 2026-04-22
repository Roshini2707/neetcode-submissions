class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate """

        count = defaultdict(int)
        res = maxCount = 0
        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res