class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums[i]-1 not in numSet -> nums[i] is starting point in sequence
        # store longest sequence length
        # loop until nums[j] not in numSet
        # count length of each sequence
        # compare with longest

        longest = 0
        numSet = set(nums)
        for num in numSet:
            # starting point
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                # compare length with longest
                longest = max(longest, length)
        
        return longest
                