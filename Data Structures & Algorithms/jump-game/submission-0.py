class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(0, len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)
        return (farthest >= len(nums) - 1)