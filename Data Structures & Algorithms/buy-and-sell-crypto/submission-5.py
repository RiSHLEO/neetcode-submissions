class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        best = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                best = max(best, prices[sell] - prices[buy])
            sell += 1
        return best 