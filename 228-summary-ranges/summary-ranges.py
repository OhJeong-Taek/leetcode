class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #to handle last element
        if not nums: return []
        nums.append(nums[-1]+2)
        
        prev = nums[0]
        start = nums[0]
        ans = []
        for i, v in enumerate(nums):
            if i==0: continue
            if v-1 != prev:
                ans.append(f"{start}->{prev}" if start != prev else f"{prev}")
                start = v
            prev = v
        
        return ans