class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = dict()
        for i, v in enumerate(nums):
            if v in m and i - m[v] <= k:
                return True
            m[v] = i
        
        return False