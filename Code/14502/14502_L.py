import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
# --------------------------------------
from collections import deque
import copy

ans = 0
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
l = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 2]

dire = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def vivi(cnt, tmp):
    if cnt == 3:
        q = deque(l)
        arr_tmp = copy.deepcopy(arr)
        while q:
            i, j = q.popleft()
            for di, dj in dire:
                ni, nj = i + di, j + dj
                if 0<=ni<n and 0<=nj<m and \
                    not arr_tmp[ni][nj]:
                    arr_tmp[ni][nj] = 2
                    q.append((ni, nj))
        global ans
        ans = max(ans, sum([i.count(0) for i in arr_tmp]))

    else:
        for k in range(tmp, n * m):
            i, j  = k//m, k%m
            if arr[i][j] == 0:
                arr[i][j] = 9
                vivi(cnt + 1, k)
                arr[i][j] = 0

vivi(0, 0)
print(ans)
