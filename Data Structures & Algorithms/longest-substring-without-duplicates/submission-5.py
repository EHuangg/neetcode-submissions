class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # add each c to charSet
        # if c already in charSet,
        # start removing characters left to right, until we remove first c
        char_set = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
                


