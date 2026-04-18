class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find first element of each sequence
        # check if i-1 is in num_set
        # if not then its the first element in the sequence
        # if it is, then keep checking if i+1, i+2, ... is in set to get seq.
        # keep track of the longest sequence length
        nums_set = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set: # start of sequence
                length = 1 # start counting
                while nums[i] + length in nums_set:
                    length += 1
                longest = max(longest, length)
            
        return longest
