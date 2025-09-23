class Solution(object):
    def maxProfit(self, prices):
        Max_prof=0
        price=10000000000000
        for i in range (len(prices)):
            if price>prices[i]:
                price=prices[i]
            else: 
                if Max_prof<prices[i]-price:
                    Max_prof=prices[i]-price
        return Max_prof

       
        
