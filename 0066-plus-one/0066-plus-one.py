class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)-1
        sum_array=[]
        sum=0
        for i in digits:
            sum+=i*10**n
            n-=1
        sum+=1
        sum=str(sum)
        for j in sum:
            sum_array.append(int(j))
        return sum_array
