class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums2={0:1}
        output=0
        a=0
        for i in nums:
            a+=i
            if a-k in nums2:
                output+=nums2[a-k]
            if a in nums2:
                nums2[a]+=1
            else:
                nums2[a]=1
            
        return output