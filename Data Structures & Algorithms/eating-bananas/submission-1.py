import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = max(piles)
        l, r = 1, most
        while l <= r:
            k = (l + r) // 2
            time = 0
            for n in piles:
                time += math.ceil(n / k)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

            