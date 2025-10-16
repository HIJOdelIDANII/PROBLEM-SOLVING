class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        zeros_list = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    zeros_list.append([i,j])
        for cord in zeros_list:
            for i in range(n):
                matrix[i][cord[1]]=0
            for j in range(m):
                matrix[cord[0]][j]=0
        return matrix
        