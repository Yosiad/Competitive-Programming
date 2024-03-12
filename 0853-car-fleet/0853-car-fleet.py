class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s={}
        d2={}
        for j in range(len(speed)):
            s[position[j]]=speed[j]
        position=sorted(list(s.keys()))
        for k in range(len(speed)):
            d2[position[k]]=s[position[k]]
        speed=list(d2.values())
        stack=[]
        for i in range(len(speed)):
            while stack and stack[-1]<=(target-position[i])/speed[i]:
                stack.pop()
            stack.append((target-position[i])/speed[i])
        return len(stack)