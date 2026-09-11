class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for id_b in range(len(prices)):
            buy = prices[id_b]
            for sell in (prices[id_b+1:]):
                tmp_profit = sell-buy
                if tmp_profit>profit:
                    profit = tmp_profit
        return profit