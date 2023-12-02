class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #min val update
        min_v = prices[0]
        ans = 0
        for p in prices:
            ans = max(ans, p - min_v)
            min_v = min(min_v, p)
            
        return ans