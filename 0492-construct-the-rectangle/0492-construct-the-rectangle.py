class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for l in range(int(area ** 0.5) + 1, 1, -1):
            w = area / l
            if not w % 1:
                w = int(w)
                return [max(l, w), min(l, w)]   
        return [area, 1]