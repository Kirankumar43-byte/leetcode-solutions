import bisect
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        starts, ends, chars = [], [], []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            starts.append(i); ends.append(j - 1); chars.append(s[i])
            i = j
        m = len(starts)
        lens = [ends[k] - starts[k] + 1 for k in range(m)]
        total_ones = sum(l for l, c in zip(lens, chars) if c == '1')
        NEG = float('-inf')
        g = [NEG] * m
        for j in range(1, m - 1):
            if chars[j] == '1':
                g[j] = lens[j - 1] + lens[j + 1]
        LOG = max(1, m.bit_length())
        sparse = [g[:]]
        k = 1
        while (1 << k) <= m:
            prev = sparse[-1]
            half = 1 << (k - 1)
            curr = [NEG] * m
            for idx in range(m - (1 << k) + 1):
                curr[idx] = max(prev[idx], prev[idx + half])
            sparse.append(curr)
            k += 1
        def range_max(l, r):
            if l > r:
                return NEG
            length = r - l + 1
            k = length.bit_length() - 1
            return max(sparse[k][l], sparse[k][r - (1 << k) + 1])
        def find_run(p):
            return bisect.bisect_right(starts, p) - 1
        ans = []
        for l, r in queries:
            a, b = find_run(l), find_run(r)
            gain = 0
            if b > a + 1:
                j1 = a + 1
                if chars[j1] == '1':
                    leftlen = ends[a] - l + 1
                    rightlen = (r - starts[b] + 1) if j1 + 1 == b else lens[j1 + 1]
                    gain = max(gain, leftlen + rightlen)
                j2 = b - 1
                if j2 != j1 and chars[j2] == '1':
                    rightlen = r - starts[b] + 1
                    leftlen = (ends[a] - l + 1) if j2 - 1 == a else lens[j2 - 1]
                    gain = max(gain, leftlen + rightlen)
                lo, hi = a + 2, b - 2
                if lo <= hi:
                    gain = max(gain, range_max(lo, hi))
            ans.append(total_ones + gain)
        return ans