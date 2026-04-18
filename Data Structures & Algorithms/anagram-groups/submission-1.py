class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through list,
        # count each letter
        # map the count to list of strings
        # return keys of dictionary

        res = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            for c in strs[i]:
                idx = ord(c) - ord('a')
                count[idx] += 1
            res[tuple(count)].append(strs[i])
        return list(res.values())


            
            