class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        res, resLen = [-1, -1], float("infinity")

        countT, countS = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        
        if resLen == float("infinity"):
            return ""
        return s[l:r + 1]
                
            
        
        