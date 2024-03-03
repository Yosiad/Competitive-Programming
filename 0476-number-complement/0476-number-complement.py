class Solution:
    def findComplement(self, num: int) -> int:
        if num==1:
            return 0
        a=int(math.log(num,2))+1
        return 2**a-num-1