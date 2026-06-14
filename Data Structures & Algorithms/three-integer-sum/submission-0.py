class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums): 
            # take care of duplicates for first pointer
            if i > 0 and n == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + n
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else: 
                    res.append([nums[left], nums[right], n])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
        return res



