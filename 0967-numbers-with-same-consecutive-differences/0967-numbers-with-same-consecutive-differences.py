class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = {i for i in range(10)}
        for _ in range(n - 1):
            new = set()
            for num in q:
                last = num % 10
                if num and 0 <= last + k <= 9:
                    new.add(num * 10 + last + k)
                if num and 0 <= last -k <= 9:
                    new.add(num * 10 + last - k)
            q = new
        return list(q)