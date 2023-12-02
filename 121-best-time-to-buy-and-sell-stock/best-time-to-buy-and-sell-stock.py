class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #min val update
        min_v = prices[0]
        ans = 0
        for p in prices:
            if p - min_v > ans: ans = p - min_v
            if p < min_v: min_v = p
            
        return ans