class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1
        
        for c in t:
            if c in dict_s:
                dict_s[c] -= 1
            else:
                return False
        
        for c in dict_s:
            if dict_s[c] != 0:
                return False
        return True