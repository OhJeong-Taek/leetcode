class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max idx update
        max_i = 0
        for i, v in enumerate(nums):
            if i > max_i: return False
            if i+v > max_i: max_i = i+v
        
        return max_i >= len(nums)-1
