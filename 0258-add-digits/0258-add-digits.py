class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        output=0
        for i in num:
            output+=int(i)
        if len(str(output))>=2:
            output=self.addDigits(output)
        return output 