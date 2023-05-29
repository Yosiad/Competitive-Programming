class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        nums1=sorted(nums)
        for i in nums:
            ans.append(nums1.index(i))
        return ans