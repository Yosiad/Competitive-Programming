class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = collections.defaultdict(int)
        ans , left, total = 0,0,0
        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            total += 1
            while len(counts) > 2:
                f = fruits[left]
                counts[f] -= 1
                total -= 1
                left += 1

                if not counts[f]:
                    counts.pop(f)
            ans = max(ans, total)
        return ans