class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap to count each word
        # use that hashmap as key
        # key must be immutable so instead use list of 26 length for each letter
        # change list to tuple
        
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            ans[tuple(count)].append(s) # key of hashmap needs to be immutable
        return list(ans.values())
