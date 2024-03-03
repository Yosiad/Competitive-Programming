class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split(' ')
        ans=''
        for i in range(len(arr)):
            arr[i]=arr[i][::-1]
        for j in arr:
            ans+=j+' '
        return ans[:-1]