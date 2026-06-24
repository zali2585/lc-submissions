class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # mark cheapest price seen yet (intialize as first)
        smallest = prices[0]
        profit = 0
        # go through each elem in list
        # if curr price is smaller than smallest, replace smallest
        # if difference between curr and smallest is larger than current largest profit, replace profit
        for i in range(len(prices)):
            curr = prices[i]
            if prices[i] < smallest:
                smallest = curr
            if curr - smallest > profit:
                profit = curr - smallest

        return profit
            
