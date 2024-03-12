class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1,st2='',''
        for i in s:
            if i=='#':st1=st1[:-1]
            else: st1+=i
        for j in t:
            if j=='#':st2=st2[:-1]
            else: st2+=j
        return st1==st2
        