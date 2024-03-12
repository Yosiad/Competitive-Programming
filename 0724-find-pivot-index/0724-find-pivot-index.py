class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums2=[]
        for i in range(len(nums)):
            if i==0:
                nums2.append(nums[0])  
            else:
                nums2.append(nums[i]+nums2[i-1])
        for j in range(len(nums2)):
            if j==0:
                if nums2[-1]==nums2[0]:
                    return 0
            else:
                if nums2[j-1]==(nums2[-1]-nums[j])/2:
                 return j
                 break
        else:
            return -1
            