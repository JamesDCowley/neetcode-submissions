class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check cols
        col_set = defaultdict(set)
        subbox_set = defaultdict(set)
        for i in range(9):
            row_set = set()
            for j in range(9):
                cell = board[i][j]
                if cell != '.':
                    subbox = self.calculateSubbox(i, j)
                    if not (0 < int(cell) < 10) or cell in col_set[j] or cell in row_set or cell in subbox_set[subbox]:
                        return False
                    col_set[j].add(cell)
                    row_set.add(cell)
                    subbox_set[subbox].add(cell)
        return True

    def calculateSubbox(self, i: int, j: int) -> int:
        subbox_x = j // 3
        subbox_y = (i // 3) * 3
        return subbox_x + subbox_y