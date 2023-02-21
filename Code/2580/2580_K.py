import sys

# x 세로줄에 n이 있는지 확인
def checkRow(x, n):
    for i in range(9):
        if n == sudoku[x][i]:
            return False
    return True

# y 가로줄에 n이 있는지 확인
def checkCol(y, n):
    for i in range(9):
        if n == sudoku[i][y]:
            return False
    return True


# x, y 좌표가 포함되어 있는 3x3 크기의 사각형의 n이 있는지 확인
def checkSq(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == sudoku[nx+i][ny+j]:
                return False
    return True

# dfs + 백트래킹
def dfs(n):
    # 스도쿠의 빈 칸을 채웠다면
    if n == len(blank):
        for _ in range(9):
            print(*sudoku[_])
        exit(0)

    # 반복문을 통해 빈칸에 1부터 9까지 넣어본다.
    for i in range(1, 10):
        x = blank[n][0] # 빈칸의 x좌표
        y = blank[n][1] # 빈칸의 y좌표

        if checkRow(x, i) and checkCol(y, i) and checkSq(x, y, i):
            sudoku[x][y] = i     
            dfs(n + 1)              # 빈 칸부터 계속 채워나감
            sudoku[x][y] = 0         # 실패했을 경우 빠져나와서 0으로 바꿔놓음

sudoku = []
blank = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])
dfs(0)