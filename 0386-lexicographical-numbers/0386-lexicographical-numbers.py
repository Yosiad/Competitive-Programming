class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output=[]
        for i in range(1,n+1):
            output.append(str(i))
        output=sorted(output)
        for i in range(len(output)):
            output[i]=int(output[i])
        return output