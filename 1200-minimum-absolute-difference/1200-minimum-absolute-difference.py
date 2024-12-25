class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        diffs={}
        arr=sorted(arr)
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] in diffs.keys(): diffs[arr[i]-arr[i-1]].append([arr[i-1], arr[i]])
            else: diffs[arr[i]-arr[i-1]]=[[arr[i-1], arr[i]]]
        return list(diffs[min(list(diffs.keys()))])