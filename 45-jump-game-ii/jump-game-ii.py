class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if nums[0] >= len(nums)-1: return 1
        
        max_i = nums[0]
        prev = max_i
        count = 1

        for i in range(1, len(nums)):
            if max_i >= len(nums)-1:
                count += 1
                break

            #max_i까지 prev update
            if i > prev:
                prev = max_i
                count += 1
            
            max_i = max(max_i, i+nums[i])

        return count