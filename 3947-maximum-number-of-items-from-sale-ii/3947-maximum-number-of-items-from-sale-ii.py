class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        mx = max(x[0] for x in items)
        freq = [0] * (mx + 1)
        for f, p in items:
            freq[f] += 1
        gain = [0] * (mx + 1)
        for f in range(1, mx + 1):
            for j in range(f, mx + 1, f):
                gain[f] += freq[j]
            gain[f] -= 1
        items.sort(key=lambda x: x[1])
        m = items[0][1]
        ans = 0
        for f, p in items:
            if p > 2 * m:
                break
            c = min(gain[f], budget // p)
            ans += 2 * c
            budget -= c * p
        ans += budget // m
        return ans