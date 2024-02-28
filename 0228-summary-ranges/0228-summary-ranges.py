class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l,ans=0,[]
        if len(nums)==0 :
            return nums
        if  len(nums)==1:
            return [str(nums[0])]
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]+1:
                if l==r-1:
                    ans.append(str(nums[l]))
                else:
                    ans.append(str(nums[l])+'->'+str(nums[r-1]))
                l=r
        if l==r: 
            ans.append(str(nums[l]))
        else:
            ans.append(str(nums[l])+'->'+str(nums[r]))
        return ans