class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(char for char in s if char.isalnum())
        new_s = new_s.lower()
        return new_s == new_s[::-1]