class Solution:
    def isPalindrome(self, s: str) -> bool:
        array=[]
        for i in s:
            if 64<ord(i)<91 or 96<ord(i)<123 :
                array.append(i.lower()) 
            if  47<ord(i)<58:
                array.append(int(i))

        return array==array[::-1]
        
