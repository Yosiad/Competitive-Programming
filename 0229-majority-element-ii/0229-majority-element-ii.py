class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans,s=[],{}
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        for j in range(len(s)):
            if list(s.values())[j]>len(nums)/3:
                ans.append(list(s.keys())[j])
        return ans