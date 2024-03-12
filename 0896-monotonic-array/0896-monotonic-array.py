class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if sorted(nums)==nums or sorted(nums)[::-1]==nums:
            return True
        return False