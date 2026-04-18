class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort O(nlogn)
        numSet = list(set(nums))
        numSet.sort()

        if len(nums) == 0:
            return 0

        longest = 1
        length = 1
        i = 1
        while i < len(numSet):
            if numSet[i] - numSet[i-1] == 1:
                length += 1
            else:
                length = 1
            longest = max(longest, length)
            i += 1
        return longest
            