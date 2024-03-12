class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        first=strs[0]
        for b in range(len(first)):
            a=ord(first[b])
            for j in strs:
                if a>ord(j[b]):
                    count+=1
                    break
                else:
                    a=ord(j[b])
        return count