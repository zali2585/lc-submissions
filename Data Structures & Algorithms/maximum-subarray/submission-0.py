class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            currSum = max(currSum + n, n)
            maxSum = max(currSum, maxSum)
        return maxSum
        
