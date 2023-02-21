import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")

#검사 해줘
def check(r, c, v):
    for i in arr[r]:
        if i == v:
            return False
        
    for i in range(9):
        if arr[i][c] == v:
            return False
    
    r //= 3
    c //= 3
    for i in range(3):
        for j in range(3):
            if arr[3*r + i][3*c + j] == v:
                return False
    return True


# # 2차원 배열로 받아줘
arr = sys.stdin.readlines()
arr = list(map(lambda x : list(map(int, x.replace("\n", "").split())), arr))

# 빈칸을 찾아줘
q = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            q.append((i, j))

# 직전의 판단이 서로에게 영향을 끼친다.... -> dfs
# 스택으로 풀어줘
visited = [[0] * 10 for _ in range(len(q))]
idx = 0
while 0<= idx < len(q):
    r, c = q[idx]
    for i in range(1, 10):
        if not visited[idx][i]:
            if check(r, c, i):
                visited[idx][i] = 1
                arr[r][c] = i
                idx += 1
                break
    else:                       # 더 갈 곳이 없다면...
        visited[idx] = [0] * 10 # 해당 depth에서 갔던 곳 초기화 해주고, 
        arr[r][c] = 0           # 가기전에 돌려놓고가~
        idx -= 1                # 뒤로 런

for i in arr:
    print(*i)