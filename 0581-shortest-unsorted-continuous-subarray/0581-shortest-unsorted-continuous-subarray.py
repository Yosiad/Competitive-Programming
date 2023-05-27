class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if sorted(nums)==nums:
            return 0
        for l in range(0,len(nums)):
            if nums[l]!=sorted(nums)[l]:
                break
        for r in range(len(nums)-1,l,-1):
            if nums[r]!=sorted(nums)[r]:
                break
        return r-l+1