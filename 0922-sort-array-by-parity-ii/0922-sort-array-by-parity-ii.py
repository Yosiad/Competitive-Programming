class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans,odd,even=[],[],[]
        for i in nums:
            if i%2==1:odd.append(i)
            else:even.append(i)
        for i in range(len(even)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans