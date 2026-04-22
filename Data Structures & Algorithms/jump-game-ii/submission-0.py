class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(0, len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
