def nqeen(row, N):
    global cnt

    if row == N: # Queen 끝까지 채움
        cnt += 1
        return
    else:
        for i in range(N):
            qlist[row] = i # row번째 행, i번째 열에 queen을 놓아본다.
            # 이후 그 행에 둔 것에 대한 유망성을 판단한다.
            for j in range(row):
                if qlist[j] == qlist[row] or row - j == abs(qlist[row] - qlist[j]): # 같은 열에 있거나 or 행 차이가 열 차이와 같을 때(대각선) 
                    break
            else:                 # 그 자리에 두어도 괜찮았다면,
                nqeen(row + 1, N) # 그 다음 행에 대해 퀸을 놓는 것을 해 본다.

n = int(input())

cnt = 0
qlist = [0] * n

nqeen(0, n)
print(cnt)