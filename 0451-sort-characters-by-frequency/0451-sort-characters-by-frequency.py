class Solution:
    def frequencySort(self, s: str) -> str:
        ans=''
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        dic=dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
        for j in range(len(dic)):
            ans+=list(dic.keys())[j]*list(dic.values())[j]
        return ans