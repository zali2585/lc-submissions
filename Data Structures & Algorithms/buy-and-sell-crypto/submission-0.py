class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        largest = prices[0]
        for i in range(len(prices)):
            curr = prices[i]
            if prices[i] < smallest:
                smallest = curr
            if curr - smallest > profit:
                largest = prices[i]
                profit = largest - smallest

        return profit
            
