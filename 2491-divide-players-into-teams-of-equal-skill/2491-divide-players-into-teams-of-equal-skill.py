class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        arr,ans,sum=[],0,skill[0]+skill[-1]
        
        for i in range(len(skill)//2):
            if not arr:arr.append(skill[i]*skill[len(skill)-i-1])
            else:
                if skill[i]+skill[len(skill)-i-1]!=sum:return -1
                else: arr.append(skill[i]*skill[len(skill)-i-1])
        for j in arr:
            ans+=j
        return ans  