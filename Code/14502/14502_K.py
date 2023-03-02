# 연구소
from collections import deque
import copy
import sys
sys.stdin = open('input.txt', 'r')

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

def bfs():
    global ans
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i, j))
    
    while q:
        ti, tj = q.popleft()

        for k in range(4):
            ni, nj = ti + di[k], tj + dj[k]
            if 0<=ni<n and 0<=nj<m and tmp_graph[ni][nj] == 0:
                tmp_graph[ni][nj] = 2
                q.append((ni, nj))

    c = 0       # 안전영역 크기
    for i in range(n):
        c += tmp_graph[i].count(0)
    ans = max(ans, c)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0
makeWall(0)
print(ans)