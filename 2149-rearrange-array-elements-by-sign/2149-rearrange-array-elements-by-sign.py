class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        for i in nums:
            if i>0:
                pos.append(i)
            if i<0:
                neg.append(i)
        ans=[]
        for j in range(len(neg)):
            ans.append(pos[j])
            ans.append(neg[j])
        return ans