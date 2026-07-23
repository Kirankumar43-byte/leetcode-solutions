class Solution:
    def uniqueXorTriplets(self, A):
        return len(A) if len(A) < 3 else 1 << (reduce(or_, A)).bit_length()