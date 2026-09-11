class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for id_b in range(len(prices)):
        #     buy = prices[id_b]
        #     for sell in (prices[id_b+1:]):
        #         tmp_profit = sell-buy
        #         if tmp_profit>profit:
        #             profit = tmp_profit
        # return profit
        profit = 0
        cheapest = prices[0]
        for id_s in range(1,len(prices)):
            # print(prices[id_s])
            sell = prices[id_s]
            
            tmp_profit = sell - cheapest
            # print(tmp_profit)
            cheapest = min(cheapest,sell)
            
            if tmp_profit>profit:
                profit = tmp_profit
        return profit