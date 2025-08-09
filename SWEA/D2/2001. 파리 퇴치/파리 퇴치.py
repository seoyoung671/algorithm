
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxcnt = 0
    for r in range(N - M + 1):         # 시작 행
        for c in range(N - M + 1):     # 시작 열
            cnt = 0
            for i in range(M):         # M 행
                for j in range(M):     # M 열
                    cnt += arr[r+i][c+j]
            maxcnt = max(maxcnt, cnt)

    print(f"#{t} {maxcnt}")