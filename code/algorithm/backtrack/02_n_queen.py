import copy


def n_queen(n):
    res = []

    def is_valid(board, row, col):
        # 检查当前列是否有冲突
        for r in board:
            if r[col]:
                return False
        # 检查左上角
        i = row
        j = col
        while i and j:
            if board[i][j]:
                return False
            i -= 1
            j -= 1

        # 检查右上角
        x = row
        y = col
        while x and y < n:
            if board[x][y]:
                return False
            x -= 1
            y += 1

        return True

    def backtrack(board, row):
        # 结束情况
        if row == n:
            res.append(board)
            return

        for col in range(n):
            #  排除不符合要求的
            if not is_valid(board, row, col):
                continue
            # 进行选择
            board[row][col] = 1
            # 进入下一层决策树
            backtrack(copy.deepcopy(board), row + 1)
            # 撤销选择
            board[row][col] = 0
    backtrack([[0]*n for _ in range(n)], 0)
    return res


ret = n_queen(8)

for r in ret:
    print(r)
