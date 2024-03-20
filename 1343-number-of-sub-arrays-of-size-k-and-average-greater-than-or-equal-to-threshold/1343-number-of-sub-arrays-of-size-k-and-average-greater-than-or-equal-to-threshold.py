class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        right=k
        sum=0
        output=0
        for j in range(k):
            sum+=arr[j]
        if sum/k>=threshold:
            output+=1
        for i in range(k,len(arr)):
            sum-=arr[left]
            sum+=arr[i]
            left+=1
            if sum/k>=threshold:
                output+=1
        return output