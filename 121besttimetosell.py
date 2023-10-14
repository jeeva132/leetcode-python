class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxpro = 0
        l,r = 0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                maxpro = max(maxpro,profit)

            else:
                l = r

            r = r+1

        return maxpro
        
