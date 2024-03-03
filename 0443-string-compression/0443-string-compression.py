class Solution:
    def compress(self, chars: List[str]) -> int:
        pre = ""
        res = []
        count = 1
        for c in chars:
            if c != pre:
                if count != 1:
                    for i in str(count):
                        res.append(i)
                res.append(c)    
                pre = c
                count = 1
            else:
                count += 1
        if count != 1:
            for i in str(count):
                res.append(i)
        n = len(res)
        chars[:] = res
        return n