def bfs(destX, destY):
    while queue:
        if arr[destX][destY] == 'S':
            return cnt[destX][destY]                # 들가기 전에 도착지인 dx, dy에 S가 도착하면 리턴
        x, y = queue.pop(0)         # first in 먼저 빼서 x, y에 대입
        for i in range(4):
            calX = x + distX[i]     # x, y 좌표에 상하좌우 해서 nx, ny 선언
            calY = y + distY[i]
            if 0 <= calX < R and 0 <= calY < C:
                # 갈려고 하는 상하좌우에 .이나 D 있고 현 위치가 S면
                if (arr[calX][calY] == '.' or arr[calX][calY] == 'D') and arr[x][y] == 'S':
                    arr[calX][calY] = 'S'       # 해당 nx, ny에 S 대입
                    queue.append((calX, calY))      # 상하좌우로 간 위치에서 계산해야 하는 좌표 큐에 삽입
                    cnt[calX][calY] = cnt[x][y] + 1     # 상하좌우에 +1씩
                if arr[calX][calY] == '.' or arr[calX][calY] == 'S' and arr[x][y] == '*': # 물 채울 차례 : x, y가 물이면
                    arr[calX][calY] = '*'           # 해당 nx, ny에 * 대입
                    queue.append((calX, calY))      # 물 채운 좌표를 큐에 재삽입
    return 'KAKTUS'

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
cnt = [[0] * C for _ in range(R)]
queue = []
distX = [-1, 1, 0, 0]
distY = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':        # 도치 위치 append
            queue.append((i, j))
        if arr[i][j] == 'D':           # Dx, Dy = Destination(도착지)
            destX = i
            destY = j

for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':            # 물 위치 append
            queue.append((i, j))


print(bfs(destX, destY))