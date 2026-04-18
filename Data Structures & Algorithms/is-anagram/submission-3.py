class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # bruteforce: sort both strings
        # compare them
        return sorted(s) == sorted(t)
            