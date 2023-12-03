class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        #to handle last element
        nums.append(nums[-1]+2)
        
        ans = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start != nums[i-1]: ans.append(f"{start}->{nums[i-1]}")
                else: ans.append(f"{nums[i-1]}")
                #ans.append(f"{start}->{nums[i-1]}" if start != nums[i-1] else f"{nums[i-1]}")
                start = nums[i]
        
        
        return ans