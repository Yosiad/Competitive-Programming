class Solution:
    def jump(self, nums: List[int]) -> int:
        cur,jumps,fart=0,0,0
        for i in range(len(nums)-1):
            fart=max(fart,i+nums[i])
            if i==cur:
                cur=fart
                jumps+=1
        return  jumps