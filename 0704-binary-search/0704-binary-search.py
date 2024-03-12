class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums=nums
        self.target=target
        if self.nums[0]>self.target or self.nums[-1]<self.target:
            return -1
        def help(start,end):
            mid=(start+end)//2
            if self.nums[mid]<self.target and self.nums[mid+1]>self.target:
                return -1
            if self.nums[mid]==self.target:
                return mid
            elif self.nums[mid]>self.target:
                return help(start,mid)
            else:return help(mid,end)
        return help(0,len(nums))