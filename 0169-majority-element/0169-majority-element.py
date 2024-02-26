class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        n=len(nums)
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        for j in range(len(s)):
            if list(s.values())[j]>n//2:
                return list(s.keys())[j]
                break