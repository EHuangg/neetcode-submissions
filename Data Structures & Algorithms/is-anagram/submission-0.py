class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = list(s)
        sort_s.sort()
        sort_t = list(t)
        sort_t.sort()
        if sort_s == sort_t:
            return True
        return False