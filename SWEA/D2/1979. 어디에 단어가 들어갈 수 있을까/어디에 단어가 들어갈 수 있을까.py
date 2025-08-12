T = int(input())

for t in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    # 행의 경우
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1


    # 열의 경우
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result +=1
    print(f"#{t} {result}")
