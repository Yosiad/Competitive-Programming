class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in nums[i+1:]+nums[:i]:
                if j>nums[i]:
                    ans.append(j)
                    break
            else: ans.append(-1)
        return ans