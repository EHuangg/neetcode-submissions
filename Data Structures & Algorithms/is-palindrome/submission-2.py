class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c
        new_s = new_s.lower()
        return new_s == new_s[::-1]