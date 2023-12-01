class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = dict()
        ans = sys.maxsize
        for idx, num in enumerate(nums):
            if num in m:
                ans = min(ans, idx-m[num])
                if ans <= k:
                    return True
            m[num] = idx
        
        return False