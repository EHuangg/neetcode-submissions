class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        neg = []
        pos = []
        zeros = []

        for n in nums:
            if n < 0:
                neg.append(n)
            elif n > 0:
                pos.append(n)
            else:
                zeros.append(n)

        neg_set = set(neg)
        pos_set = set(pos)

        # 1 zero: [-n, 0, n]
        if len(zeros) >= 1:
            for n in pos_set:
                if (-n) in neg_set:
                    ans.append([-n, 0, n])

        # 3 zeros: [0, 0, 0]
        if len(zeros) >= 3:
            ans.append([0, 0, 0])
        
        # Two negative, one positive
        for i in range(len(pos)):
            target = -pos[i]
            seen = set()
            for j in range(len(neg)):
                diff = target - neg[j]
                if diff in seen:
                    res = sorted([pos[i], neg[j], diff])
                    if res not in ans:
                        ans.append(res)
                seen.add(neg[j])
        
        # Two positive, one negative
        for i in range(len(neg)):
            target = -neg[i]
            seen = set()
            for j in range(len(pos)):
                diff = target - pos[j]
                if diff in seen:
                    res = sorted([neg[i], pos[j], diff])
                    if res not in ans:
                        ans.append(res)
                seen.add(pos[j])
        
        return ans