class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        dicc = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in dicc.values():
                list.append(i)
            elif list and dicc[i]==list[-1]:
                list.pop()
            else:
                return False
        return list==[]