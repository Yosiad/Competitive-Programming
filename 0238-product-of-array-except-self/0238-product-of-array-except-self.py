class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]
        a=1
        for i in range(len(nums)-1):
            a*=nums[i]
            output.append(a)
        a=1
        for j in range(len(nums)-1,0,-1):
            a*=nums[j]
            output[j-1]=output[j-1]*a
        return output