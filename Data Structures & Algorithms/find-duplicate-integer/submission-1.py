class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # map indices to values 
        # fake create a linked list through array

        slow = nums[0]
        fast = nums[0]
        # enter cycle (not necessarily duplicate)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # finding entrance
        # fast traveled 2x as much as slow 
        # distance from start to entrance = x # of complete cycles
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        # they will land on same bc distance from meeting point to start = distance from start to entrance
        return slow
