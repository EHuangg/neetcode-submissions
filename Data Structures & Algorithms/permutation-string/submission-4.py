class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        # counting s1
        for c in s1:
            s1Count[ord(c)-ord('a')] += 1
        
        # going through s2
        for r in range(len(s1), len(s2) + 1):
            l = r - len(s1)
            
            s2Count = [0] * 26
            #counting window
            for i in range(l, r):
                s2Count[ord(s2[i]) - ord('a')] += 1
            print((l, r),s2Count)
            if s1Count == s2Count:
                return True
        return False 


                    