class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        b = 0
        for i in pushed:
            stack.append(i)
            while stack!=[] and b<len(pushed) and popped[b]==stack[-1]:
                 stack.pop()
                 b+=1
        return stack==[]