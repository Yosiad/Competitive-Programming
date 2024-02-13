class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums=sorted(nums)
        if nums[2]>=nums[1]+nums[0]: return "none"
        if len(set(nums))==1: return "equilateral"
        if len(set(nums))==2: return "isosceles"
        else: return "scalene"