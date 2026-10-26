class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r_size = len(matrix)
        c_size = len(matrix[0]) 
        row_zeros_set = set()
        column_zeros_set = set()
        for r in range(r_size):
            for c in range(c_size):
                num = matrix[r][c]
                if num == 0:
                    row_zeros_set.add(r)
                    column_zeros_set.add(c)
        for r in range(r_size):
            for c in range(c_size):
                if r in row_zeros_set:
                    matrix[r][c]=0
                if c in column_zeros_set:
                    matrix[r][c]=0
        