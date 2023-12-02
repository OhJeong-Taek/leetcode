class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #min, max val update
         
        min_v = sys.maxsize
        ans = 0
        for p in prices:
            ans = max(ans, p - min_v)
            min_v = min(min_v, p)
            
        return ans