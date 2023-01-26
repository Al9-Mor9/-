import sys
sys.stdin = open("input.txt", "r")
#-------------------------------------
from collections import deque
#인풋 받기
R, C = map(int, input().split())
m = [list(input()) for _ in range(R)]

#맵 프린트
for r in m:
    print(r)

#변수 선언
visited = [[0] * C for _ in range(R)]
q = deque()
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 'KAKTUS'
chaser = 0

#주어진 위치 q에 저장.
# q.pop() => [row, column, type, depth] depth는 문제에서 보면 minute, 시간과 같다. 
for r in range(R):
    for c in range(C):
        if m[r][c] == '.':
            continue
        elif m[r][c] == '*':
            q.appendleft([r, c, '*', 0])
            visited[r][c] = 1
        elif m[r][c] == 'D':
            D = [r, c]
        elif m[r][c] == 'S':
            q.append([r, c, 'Beaver', 0])
            visited[r][c] = 1
        else:
            continue

#initialized 확인
print("\n----initialization----\nq : ", q)
for v in visited:
    print(v)
print("----------------------")

while q:
    r, c, x, depth = q.popleft()    #왼쪽에서 빼고, 오른쪽에 쌓는다. 
                                    #depth가 낮은 애들부터 탐색할 수 있다. 
    if D == [r, c]:
        ans = depth
        break
    else:
        for dx, dy in d:                    #4방향 탐색을 물, 비버에 대해 해준다.
            r_, c_ = r + dx, c + dy         #물이 먼저 가고, 그 기록은 visited에 저장한다.
            if -1 < r_ < R and \
                -1 < c_ < C and \
                visited[r_][c_] == 0 and \
                m[r_][c_] != 'X':

                if x == '*' and [r_, c_] != D:             #꺼낸 q가 물일 경우
                    q.append([r_, c_, '*', depth + 1])
                    visited[r_][c_] = 2
                
                if x == 'Beaver' and m[r_][c_] != '*':          #꺼낸 q가 비버일 경우
                    q.append([r_, c_, 'Beaver', depth + 1])
                    visited[r_][c_] = 1
    #q 추적용.
    
    if depth > chaser:
        print(f'\ndepth : {depth}')
        print("q : ", q)
        for v in visited:
            print(v)
        chaser = depth

print("\nanswer is ...",ans)

