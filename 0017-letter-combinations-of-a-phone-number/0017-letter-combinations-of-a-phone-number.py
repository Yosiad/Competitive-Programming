class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        array=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result=[]
        if len(digits)==0:
            result=[]
        if len(digits)==1:
            for i in array[int(digits)-2]:
                result.append(i)
        if len(digits)==2:
            for i in array[int(digits[0])-2]:
                for j in array[int(digits[1])-2]:
                    result.append(i+j)
        if len(digits)==3:
            for i in array[int(digits[0])-2]:
                for j in array[int(digits[1])-2]:
                    for k in array[int(digits[2])-2]:
                        result.append(i+j+k)
        if len(digits)==4:
            for i in array[int(digits[0])-2]:
                for j in array[int(digits[1])-2]:
                    for k in array[int(digits[2])-2]:
                        for c in array[int(digits[3])-2]:
                            result.append(i+j+k+c)
        return result