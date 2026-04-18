class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        smallest = min(nums)
        largest = max(nums)
        nums = set(nums)

        count = ans = 0

        for n in range (smallest, largest + 1):
            if n in nums:
                count += 1
            else:
                ans = max(count, ans)
                count = 0 
        return max(ans, count)