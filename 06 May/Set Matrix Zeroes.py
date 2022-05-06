# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

class Solution(object):
    def setZeroes(self, matrix):

        m, n = len(matrix), len(matrix[0])
        
        row_zeros = set()
        col_zeros = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row_zeros or j in col_zeros:
                    matrix[i][j] = 0
