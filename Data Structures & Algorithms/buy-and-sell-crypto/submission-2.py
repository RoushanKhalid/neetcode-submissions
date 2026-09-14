class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0

        for i in range(len(prices)):
            buy = prices[i]
            new_list = prices[i:]

            sell = max(new_list)
            profit = sell - buy

            if profit > maximum:
                maximum = profit

        return maximum