class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1: return [[1]]
        if numRows==2: return [[1],[1,1]]
        output=[[1],[1,1]]
        ans=[1,1]
        for i in range(numRows-2):
            tmp=[]
            tmp.append(1)
            for i in range(len(ans)-1):
                tmp.append(ans[i]+ans[i+1])
            tmp.append(1)
            ans=tmp
            output.append(ans)
        return output