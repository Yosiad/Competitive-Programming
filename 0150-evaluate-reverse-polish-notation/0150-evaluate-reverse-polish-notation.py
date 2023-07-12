class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for element in tokens:
            if element=="+":
                stack.append(stack.pop()+stack.pop())
            elif element=="*":
                stack.append(stack.pop()*stack.pop())
            elif element=="-":
                first=stack.pop()
                second=stack.pop()
                stack.append(second-first)
            elif element=="/":
                first=stack.pop()
                second=stack.pop()
                stack.append(int(second/first))
            else:
                stack.append(int(element))
        return stack[0]