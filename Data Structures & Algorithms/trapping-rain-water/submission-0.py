class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL <= maxR:
                curr = maxL - height[l]
                l += 1
            else:
                curr = maxR - height[r]
                r -= 1
            if curr > 0:
                area += curr
        return area

        

