class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0

        for i in range(len(prices)):
            lowest = prices[i]
            min_ind = i

            new_list = prices[min_ind:]

            highest = max(new_list)
            profit = highest - lowest

            if profit > maximum:
                maximum = profit

        return maximum