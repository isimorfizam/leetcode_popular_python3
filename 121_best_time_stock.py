import numpy as np
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    # BAD BECAUSE OF np.array - np.array : it adds O(N) complexity within O(N) loop making it O(N2)
    #     best = 0
    #     previous = prices[0]
    #     for cnt in range(0,len(prices)-1) :
    #         if cnt>0 :
    #             # if greater than previous one, there is already a better option
    #             if prices[cnt]>previous:
    #                 continue
    #             else : 
    #                 previous = prices[cnt]
    #         prices_after = np.array(prices[cnt+1:]) - prices[cnt]*np.ones(len(prices[cnt+1:]))
    #         # to rule out negative numbers
    #         best_new = max(max(prices_after), 0)
    #         # if better then pervious best, you are now best
    #         best = max(best, best_new)
    #     return int(best)

    def maxProfit(self, prices: List[int]) -> int:
        # Greedy search
        l = 0 
        r = 1
        best = 0 
        while r < len(prices):
            if prices[l]>prices[r]:
                l = r
                r = l + 1
            else :
                dif = prices[r] - prices[l]
                best = max(best,dif)
                r = r + 1
        return best

    def maxProfit2(self, prices: List[int]) -> int:
        # example to look at [7,2,9,1,3,4]
        max_profit = 0
        min_value = float('inf')
        for i in prices:
            # if minimum value -> means it's definitely better than previous -> calculate difference only if next is bigger
            if (i <= min_value):
                min_value = i
            # if not minimum value, calculate difference with minimum value 

            elif (i - min_value > max_profit):
                max_profit = i - min_value
        return max_profit