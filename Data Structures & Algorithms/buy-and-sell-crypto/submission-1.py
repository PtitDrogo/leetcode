class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small, maxProfit = 101, 0
        for num in prices:
            if num < small:
                small = num
            else:
                maxProfit = max(num - small, maxProfit)
        return maxProfit