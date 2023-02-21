import sys
sys.stdin = open("input.txt", "r")

# 개 억지 bfs 실패 후 dfs로 노선 변경
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
n, m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append([*input()])

v = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
m_d = 0

def dfs(r, c, d):
    global m_d
    m_d = max(m_d, d)
    for i in range(4):
        r_ = r + int(arr[r][c]) * dx[i]
        c_ = c + int(arr[r][c]) * dy[i]
        if 0 <= r_ < n and 0 <= c_ < m and \
                arr[r_][c_] != "H" and \
                d + 1 > dp[r_][c_]:
            if v[r_][c_]:
                print(-1)
                exit()
            else:
                dp[r_][c_] = d + 1
                v[r_][c_] = True
                dfs(r_, c_, d + 1)
                v[r_][c_] = False
dfs(0, 0, 0)
print(m_d + 1)