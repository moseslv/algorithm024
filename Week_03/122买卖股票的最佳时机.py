#!/usr/bin/env python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, profit = float('inf'),0
        if n<=1:return 0
        for i in range(1,n): # 不限制交易次数，需要做判断
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit