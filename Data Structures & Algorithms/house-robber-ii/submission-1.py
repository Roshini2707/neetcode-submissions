class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))
            
        
    def rob_linear(self, nums: List[int]) -> int:
        rob1 , rob2 = 0, 0
        for i in nums:
            temp = max((i+rob1), rob2)
            rob1 = rob2
            rob2 = temp
        return rob2  
        