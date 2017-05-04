class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])

        queue = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append([i, j])
                else:
                    matrix[i][j] = 10000

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while len(queue):
            cell = queue.pop(0)
            for d in dirs:
                x = cell[0] + d[0]
                y = cell[1] + d[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[cell[0]][cell[1]] + 1:
                    continue
                else:
                    matrix[x][y] = matrix[cell[0]][cell[1]] + 1
                    queue.append([x, y])

        return matrix