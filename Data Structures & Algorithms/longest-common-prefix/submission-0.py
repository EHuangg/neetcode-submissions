class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if s[0:i+1] != prefix + c:
                    return prefix
            prefix += c
        return prefix
