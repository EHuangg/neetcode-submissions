class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force:
        max_difference = 0
        # iterate through each item, set them as the starting date
        for i in range(len(prices)):
            buy = prices[i]
        # then iterate through the other days and check for the max difference
            for j in range(i+1, len(prices)):
                sell = prices[j]
                # check if max difference is bigger than 0
                max_difference = max(max_difference, sell-buy)
        return max_difference
        