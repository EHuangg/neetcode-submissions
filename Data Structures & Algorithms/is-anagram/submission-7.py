class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make two dicts, map number of each letter -> letter
        if len(s) != len(t):
            return False
        str_dict = {}
        # counting each char in s
        for c in s:
            if c in str_dict:
                str_dict[c] += 1
            else:
                str_dict[c] = 1
        
        # compare with t
        for c in t:
            if c in str_dict:
                str_dict[c] -= 1
                if str_dict[c] == 0:
                    del str_dict[c]
            else:
                return False

        
        # check if str_dict is all zero
        return True
            