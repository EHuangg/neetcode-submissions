class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = min(prices) - max(prices)
        
        for i in range (0, len(prices)):
            if i + 1 >= len(prices):
                return current_max
            for j in range (i, len(prices)):
                print(prices[j], prices[i])
                if prices[j] - prices[i] >= current_max:
                    current_max = prices[j] - prices[i]

        return current_max