class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        a=0
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        s=dict(sorted(s.items(), key=lambda x:x[1], reverse=True))        
        return list(s.keys())[:k]