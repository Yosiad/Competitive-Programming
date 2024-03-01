class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums=sorted(nums)[::-1]
        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0]