class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(9)]
        column_sets = [set() for i in range(9)]
        # subgrid_sets = [[set() for i in range(3)] for j in range(3)]
        subgrid_sets = [set() for i in range(9)]
        # print(subgrid_sets)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.': 
                    continue
                grid_num = 3*(r//3)+c//3

                if num in row_sets[r]:
                    return False
                elif num in column_sets[c]:
                    return False
                elif num in subgrid_sets[grid_num]:
                    return False

                row_sets[r].add(num)
                column_sets[c].add(num)
                subgrid_sets[grid_num].add(num)
        return True