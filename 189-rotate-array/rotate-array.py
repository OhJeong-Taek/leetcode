class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        """
        Do not return anything, modify nums in-place instead.
        """
        