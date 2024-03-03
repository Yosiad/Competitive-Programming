class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater=[]
        for i in nums1:
            a=nums2.index(i)
            for j in range(a, len(nums2)):
                if nums2[j]>i:
                    greater.append(nums2[j])
                    break
            else:
                greater.append(-1)
        return greater