import sys
sys.stdin = open('text.txt', 'r')
#####
import sys
input = sys.stdin.readline
def check(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for k in range(9):
        if a == arr[x][k] or a == arr[k][y]:
            return False
    for l in range(3):
        for m in range(3):
            if a == arr[nx + l][ny + m]:
                return False
    return True

def dfs(idx):
    if idx == len(stack):
        for ind in arr:
            print(*ind)
        exit(0)
    x, y = stack[idx]
    for num in range(1, 10):
        if check(x, y, num):
            arr[x][y] = num
            dfs(idx + 1)
            arr[x][y] = 0


n = 9
arr = [list(map(int, input().split())) for _ in range(n)]
stack = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            stack.append([i, j])

dfs(0)