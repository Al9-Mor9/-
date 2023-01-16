num = int(input())

if num < 100:       # 두자리수 이하의 숫자는 전부 한수
    print(num)
else:               # 100 이상
    cnt = 99
    if num<=1000:
        for i in range(num, 99, -1): # 숫자 하나씩 list 삽입
            arr = []
            j = i
            while j >= 1:
                arr.insert(0, j % 10)
                j //= 10
            # 기본 3자리수부터일테니 0-1, 1-2 비교
            if (arr[0] - arr[1]) == (arr[1] - arr[2]):
                cnt += 1

    print(cnt)
