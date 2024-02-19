class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency={}
        for task in tasks:
            if task not in frequency:
                frequency[task]=1
            else:
                frequency[task]+=1
        frequency=[value for key, value in frequency.items()]
        max_f=max(frequency)
        max_f_tasks=frequency.count(max_f)
        return max(len(tasks),(max_f-1)*(n+1)+max_f_tasks)
    
