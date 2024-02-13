class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, _sum=int(str(n)[0]), int(str(n)[0])
        for num in str(n)[1:]:
            product*=int(num)
            _sum+=int(num)
        return product-_sum