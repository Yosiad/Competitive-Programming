class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        second,first=1,1
        count=0
        nums=[second]
        while(second<=k): 
            nums.append(second)
            tmp=first
            first=second 
            second+=tmp 
        print(nums)
        for num in nums[::-1]:
            if k>=num:
                count+=1
                k-=num
                print(num)
        return count  
    
    