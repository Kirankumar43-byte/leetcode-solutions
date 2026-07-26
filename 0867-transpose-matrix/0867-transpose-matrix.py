class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        result=[]
        for i in range (len(matrix[0])):
            result.append([])
            for j in range (len(matrix)):
                result[i].append(matrix[j][i])
        return result