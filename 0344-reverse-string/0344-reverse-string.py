class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        while i<len(s)-1:
            s.insert(len(s)-i,s[0])
            s.pop(0)
            i+=1