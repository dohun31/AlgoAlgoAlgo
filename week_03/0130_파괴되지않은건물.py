def apply_skill(dp, r1, c1, r2, c2, degree):
    dp[r1][c1] += degree
    dp[r1][c2 + 1] -= degree
    dp[r2 + 1][c1] -= degree
    dp[r2 + 1][c2 + 1] += degree

def solution(board, skill):
    row, col = len(board), len(board[0])
    dp = [[0 for _ in range(col + 2)] for _ in range(row + 2)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: degree = -degree
        apply_skill(dp, r1 + 1, c1 + 1, r2 + 1, c2 + 1, degree)

    cnt = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            if board[i - 1][j - 1] + dp[i][j] > 0: cnt += 1

    return cnt