#import sys
#sys.stdin = open("input.txt", "r")

def binary_search(li, c):
    l = 0 
    r = len(li) - 1
    while l <= r:
        mid = int((l+r)/2)
        if li[mid] == c:
            return 1
        elif li[mid] > c:
            r = mid - 1
        else:
            l = mid + 1
    return 0


n = int(input())
a_n = list(map(int, input().split()))
a_n.sort()

m = int(input())
a_m = list(map(int, input().split()))

for i in a_m:
    print(binary_search(a_n, i))

