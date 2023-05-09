class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i,a in enumerate(nums):
            l,r=i+1,len(nums)-1
            if i>0 and a==nums[i-1]:
                continue
            while l<r:
                if a+nums[l]+nums[r]>0:
                    r-=1
                elif a+nums[l]+nums[r]<0:
                    l+=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans