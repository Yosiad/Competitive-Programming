class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=sorted(gifts)[::-1]
        for i in range(k):
            gifts[0]=int(math.sqrt(gifts[0]))
            gifts=sorted(gifts)[::-1]
        print(gifts)
        return sum(gifts)