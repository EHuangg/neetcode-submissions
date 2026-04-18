class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        offset = l
        
        def binary_search(l, r, target):
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1
        
        left_half_search = binary_search(0, offset-1, target)
        if left_half_search != -1:
            return left_half_search
        else:
            return binary_search(offset, len(nums)-1, target)
        