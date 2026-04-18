class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0

        ans = [0] * len(height)
        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                ans[l] = maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                ans[r] = maxR - height[r]
                r -= 1
        
        return sum(ans)
            
        
