class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def find(nums):
            if len(nums)==1: return nums[0]
            if len(nums)==2: return max(nums[0],nums[1])
            nums[len(nums)-3]=nums[len(nums)-3]+nums[-1]
            for i in range(len(nums)-4,-1,-1):
                nums[i]=max(nums[i+2]+nums[i],nums[i+3]+nums[i])
            return max(nums[0],nums[1])
        return max(find(nums[1:]),find(nums[:-1]))