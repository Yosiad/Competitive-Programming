class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(sorted(list(map(int,nums)),reverse=True)[k-1])