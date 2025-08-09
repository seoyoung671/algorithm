
T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxcnt = 0
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j] # 현재 위치의 파리 갯수
            for l in range(1,M):
                for dx, dy in [0,1],[1,0],[0,-1],[-1,0]:
                    x = i + dx*l
                    y = j + dy*l
                    if 0 <= x < N and 0<= y < N:
                        cnt += arr[x][y]
            maxcnt = max(maxcnt,cnt)

    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]  # 현재 위치의 파리 갯수
            for l in range(1, M):
                for dx, dy in [1, 1], [1, -1], [-1, -1], [-1, 1]:
                    x = i + dx * l
                    y = j + dy * l
                    if 0 <= x < N and 0 <= y < N:
                        cnt += arr[x][y]
            maxcnt = max(maxcnt, cnt)
    print(f"#{t} {maxcnt}")
