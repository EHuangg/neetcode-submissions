class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        # counting frequency per letter in s
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        # comparing letter frequency in s to t
        for c in t:
            if c in s_dict:
                s_dict[c] -= 1
            else:
                return False

        # check if each letter in s_dict has frequency 0
        for c in s_dict:
            if s_dict[c] != 0:
                return False
        return True

