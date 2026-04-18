class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers, move whichever bar is smaller
        # because we are limited by the shorter wall
        l, r = 0, len(heights) - 1
        largest = area = 0
        
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            largest = max(largest, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max(largest, area)
            