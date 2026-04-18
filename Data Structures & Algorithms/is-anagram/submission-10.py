class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        
        for c in t:
            if c in s_dict and s_dict[c] >= 1:
                s_dict[c] -= 1
            else:
                return False
        return True

