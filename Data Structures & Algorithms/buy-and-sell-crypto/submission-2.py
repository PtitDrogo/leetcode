class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMinPrice = 101
        profit = 0
        for price in prices:
            currMinPrice = min(price, currMinPrice)
            profit = max(price - currMinPrice, profit)
        return profit