class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        elif len(nums)==2:
            return str(nums[0])+'/'+str(nums[1])
        else:
            ans=str(nums[0])+'/('+str(nums[1])
            for i in range(2,len(nums)):
                ans+='/'+str(nums[i])
        return ans+')'