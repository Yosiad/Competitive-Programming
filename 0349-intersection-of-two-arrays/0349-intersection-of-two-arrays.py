class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    if i in output:
                        continue
                    output.append(i)
        return output