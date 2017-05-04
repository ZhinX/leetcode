class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 10000
                    left = 10000
                    top = 10000
                    if i > 0:
                        left = min(10000, matrix[i - 1][j])
                    if j > 0:
                        top = min(10000, matrix[i][j - 1])
                    matrix[i][j] = min(left, top) + 1

        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if matrix[i][j] != 0:
                    right = 10000
                    bottle = 10000
                    if i < m - 1:
                        right = matrix[i + 1][j]
                    if j < n - 1:
                        bottle = matrix[i][j + 1]
                    matrix[i][j] = min(matrix[i][j], min(right, bottle) + 1)

        return matrix