#행 : depth
#열 : r[depth]
def DFS(depth):
    global cnt
    if depth == n:
        cnt += 1

    else:
        for candidate in range(n):
            if visit[candidate]:
                continue
            r[depth], a = candidate, 1
            for pre_depth in range(depth):
                if r[depth] == r[pre_depth] or \
                abs(r[depth] - r[pre_depth]) == depth - pre_depth: \
                a = 0
            if a == 1:
                visit[candidate] = True
                DFS(depth + 1)
                visit[candidate] = False

n = int(input())
cnt = 0 
r = [0] * n
visit = [False] * n

DFS(0)
print(cnt)

