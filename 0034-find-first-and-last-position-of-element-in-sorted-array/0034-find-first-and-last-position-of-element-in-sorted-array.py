class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fi,f,se,s=0,0,len(nums)-1,len(nums)-1
        if not nums or nums[0]>target or nums[-1]<target: return [-1,-1]
        mid=-1
        while fi<=se:
            mid=(fi+se)//2
            if nums[mid]==target and (mid==0 or nums[mid-1]!=target): break
            elif (nums[mid]<target and nums[mid+1]>target) or ((mid==0 or mid==len(nums)-1) and len(nums)>2):
                mid=-1 
                break
            elif nums[mid]==target or nums[mid]>target: se=mid-1
            else: fi=mid+1
        if mid==-1: return [-1,-1]
        while f<=s: 
            l=(f+s)//2
            if nums[l]==target and (l==len(nums)-1 or nums[l+1]!=target): break
            elif nums[l]>target: s=l-1
            else: f=l+1
        return [mid,l]           