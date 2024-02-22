class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:return 0
        if target>nums[-1]:return len(nums)
        self.target=target
        self.nums=nums
        def help(a,b):
            c=(a+b)//2
            if self.nums[c]==self.target:
                return c
            elif self.nums[c]<self.target and self.nums[c+1]>self.target:
                return c+1
            elif self.nums[c]<self.target:
                return help(c,b)
            else: return help(a,c)
        return help(0,len(nums))