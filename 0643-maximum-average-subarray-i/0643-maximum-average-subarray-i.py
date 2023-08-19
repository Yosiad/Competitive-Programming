class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums=0
        for i in range(k):
            sums+=nums[i]
        max_sum=sums
        for j in range(k,len(nums)):
            sums+=nums[j]
            sums-=nums[j-k]
            max_sum=max(max_sum,sums)
        return max_sum/k