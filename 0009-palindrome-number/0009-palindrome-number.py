class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        return int(str(x)[::-1])==x