class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices down -> lower_v update
        # price up -> sell -> lower_v, ans update
        lower_v = prices[0]
        ans = 0
        for p in prices:
            if p < lower_v: lower_v = p
            if p > lower_v:
                ans += p - lower_v
                lower_v = p
        return ans

