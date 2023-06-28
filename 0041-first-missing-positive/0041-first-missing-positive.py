class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=0
        nums=sorted(nums)
        if nums[0]>1 or nums[-1]<=0:
            a=1
        else:
            for i in range(len(nums)-1):
                if nums[i]>=0 and nums[i+1]-nums[i]>1:
                    a=nums[i]+1
                    break
                if nums[i]<1 and nums[i+1]>1:
                    a=1
                    break
        if a==0:
            a=nums[-1]+1
        return a