class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            char_set = {s[i]}
            j = i + 1
            while j < len(s) and s[j] not in char_set:
                char_set.add(s[j])
                j += 1
            longest = max(longest, len(char_set))
        return longest