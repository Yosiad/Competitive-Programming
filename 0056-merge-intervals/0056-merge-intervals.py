class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals=sorted(intervals)
        l,r=intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if r>=intervals[i][0]:
                l=min(l,intervals[i][0])
                r=max(r,intervals[i][1])
            else:
                ans.append([l,r])
                l,r=intervals[i][0],intervals[i][1]
        ans.append([l,r])
        return ans