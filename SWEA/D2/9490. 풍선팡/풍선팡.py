
T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxsum = 0 # 최댓값 초기화

    # 모든 행렬 값에 대해 순회
    for x in range(N):
        for y in range(M):
            # sumresult 초기화
            sumresult = arr[x][y]
            length = arr[x][y]
            for l in range(1,length+1):
                for dx, dy in [0,1],[1,0],[0,-1],[-1,0]:
                    nx, ny = x + dx*l, y + dy*l
                    if 0 <= nx < N and 0 <= ny < M:
                        sumresult += arr[nx][ny]
            maxsum = max(maxsum,sumresult)

    print(f"#{t} {maxsum}")