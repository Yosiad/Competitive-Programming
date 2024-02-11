class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [0, 0] + [1] * (n - 1) 
        for k in range(ceil(n**0.5) + 1):
            if sieve[k]:
                for i in range(k*k, n+1, k):
                    sieve[i] = 0
                                 
        return sum(sieve[:-1])