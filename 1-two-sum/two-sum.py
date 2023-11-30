class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, x in enumerate(nums):
            m[x] = i

        for i, x in enumerate(nums):
            if target - x in m and m[target-x] != i:
                return [i, m[target-x]]