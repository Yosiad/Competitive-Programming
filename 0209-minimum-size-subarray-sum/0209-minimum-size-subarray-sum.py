class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=len(nums)+1
        l=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]                
            while sum>=target:
                length=min(length, i+1-l)
                sum-=nums[l]
                l+=1
            
        return 0 if length==len(nums)+1 else length