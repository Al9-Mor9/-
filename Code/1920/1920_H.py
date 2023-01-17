N = int(input())
list_N = list(map(int, input().split()))
list_N.sort()
M = int(input())
list_M = list(map(int, input().split()))

def binary_search(search):
    head = 0
    tail = N - 1
    while head <= tail:
        middle = (head + tail) // 2
        if list_N[middle] == search:
            return True

        if search < list_N[middle]:
            tail = middle - 1
        elif search > list_N[middle]:
            head = middle + 1


for i in range(M):
    if binary_search(list_M[i]):
        print(1)
    else:
        print(0)

"""
for i in range(M):
    print(1) if list_M[i] in list_N else print(0)
"""