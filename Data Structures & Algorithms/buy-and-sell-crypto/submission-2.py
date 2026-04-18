class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        # have left and right pointer
        l, r = 0, 0 # indices of buy and sell dates
        while r < len(prices):
        # compare left and right,
        # if left > right, then any potential profit would be bigger starting from right
            if prices[l] > prices[r]:
        # so set left = right
                l = r
        # other wise, compare maxProfit with right - left, save bigger number
            else:
                maxP = max(maxP, prices[r] - prices[l])
            r += 1
        return maxP