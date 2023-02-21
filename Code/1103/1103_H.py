import sys
sys.stdin = open('text.txt', 'r')
#####

def dfs(x, y):
    global flag, visited
    # for i in visited:
    #     print(i)
    # print()
    if not (0 <= x < n and 0 <= y < m) or arr[x][y] == 'H':
        return 0    # 더 못가면 리턴
    if visited[x][y]:  # 이미 방문 했다면 무한루프 가능, -1 리턴
        flag = True    # 플래그 올림
        return -1

    # 이미 해당 위치에서부터 도착점까지 갈 수 있는 최대 이동횟수를 계산한적 있으면
    # 그 값을 그대로 반환하여 중복계산 제거 (DP)
    if dp[x][y] != -1:
        return dp[x][y]

    visited[x][y] = 1
    val = int(arr[x][y])
    for dr in range(4): # delta
        nx = x + dx[dr] * val
        ny = y + dy[dr] * val
        # 해당 점에서 갈 수 있는 최댓값 갱신
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        if flag:   # 반복있으면 return -1
            return -1

    # 방문 안한걸로 하고 다시 dfs 돌릴려면 넣어야함
    visited[x][y] = 0
    # dp[x][y] 갱신 했으면 다시 리턴
    return dp[x][y]


n, m = map(int, input().split())
arr = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
flag = False   # 무한루프 확인용 플래그
print(dfs(0, 0))
