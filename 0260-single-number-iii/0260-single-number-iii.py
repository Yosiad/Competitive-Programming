class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        if nums[0] !=nums[1]:
            ans.append(nums[0])
        if nums[-1]!=nums[-2]:
            ans.append(nums[-1])
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                ans.append(nums[i])
            if len(ans)==2:
                break
        return ans