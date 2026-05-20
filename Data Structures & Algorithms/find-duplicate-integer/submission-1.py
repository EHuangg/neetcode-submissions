class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)
        for n in nums:
            seen[n] += 1
            if seen[n] >= 2:
                return n
            