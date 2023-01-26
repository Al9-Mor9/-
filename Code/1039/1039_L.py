#bfs 말고 그리디하게 접근하려다 자꾸 에러떠서 포기

# - bfs 대신 k번 교환하여 최대값을 찾는다
#1. 동일 숫자면 교환해도 상관이 없는지 (값은 동일)
#2. 다른 숫자여도 여러번 반복해서 교환해도 되는지

import sys 
sys.stdin = open("input.txt", "r")
#
'''
0으로 시작하지 않는 정수 N이 주어진다. 이때, M을 정수 N의 자릿수라고 했을 때, 

다음과 같은 연산을 K번 수행한다. 1 ≤ i < j ≤ M인 i와 j를 고른다. 

그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 이때, 바꾼 수가 0으로 시작하면 안 된다.

위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.'''
n, k = input().split()
m = len(n)
k = int(k)
is_bool = False
# 맨 앞자리 외 모두 0 or 10보다 작을 경우 -1 출력
if int(n) < 10:
    print(-1)
elif int(n[1:]) == 0:
    print(-1)
else:
    n = list(n)
    idx = 0
#    print(n, k, m)
#    print('------------')
    while k:
        #바꿀 자리는 높은 자리부터 선택
        val = int(n[idx])
        tmp, tmp_i = 0, idx

        #낮은 자리부터 가장 큰 수 탐색
        for r in range(m-1, idx, -1):
            if tmp < int(n[r]):
                tmp, tmp_i = int(n[r]), r
        
        #idx가 가리키는 값보다 tmp로 찾은 값이 더 크다면, 바꾸어준다.
        if val > tmp:
            idx += 1
        elif val == tmp:
            idx += 1
            is_bool = True
        else:
            n[idx], n[tmp_i] = n[tmp_i], n[idx]
            idx += 1
            k -= 1
        print(n, m, k, idx)

        #다 정렬했는데 교환 횟수가 남는다면... 최소만 진동시킨다. 다만 같은 수를 바꿀 수는 없다.
        #같은 수끼리 교환해도 된다니...
        # if idx == m - 2 and k > 0:
        #     if k % 2 == 1 and is_bool == False:
        #         n[-1], n[-2] = n[-2], n[-1]
        #         k = 0
        #     else:
        #         k = 0 
    #print(int(''.join(s for s in n)))

        if idx == m - 2 and k > 0:
            print('in')
            if k % 2 == 1:
                for i in range(m - 2, -1, -1):
                    if int(n[i]) != int(n[i+1]):
                        n[i], n[i+1] = n[i+1], n[i]
                        k = 0
                        break
            else:
                k = 0
                break
    print(int(''.join(s for s in n)))

