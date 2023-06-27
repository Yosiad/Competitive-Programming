class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]
        if rowIndex==1: return [1,1]
        ans=[1,1]
        for i in range(rowIndex-1):
            tmp=[]
            tmp.append(1)
            for i in range(len(ans)-1):
                tmp.append(ans[i]+ans[i+1])
            tmp.append(1)
            ans=tmp
        return ans
        