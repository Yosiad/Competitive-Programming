class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        equal=[]
        for i in nums:
            if i>pivot:
                right.append(i)
            elif i<pivot:
                left.append(i)
            else:
                equal.append(i)
        return left+equal+right