T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxsum = 0
    for i in range(N):
        for j in range(N):
            tmpsum = 0
            for k in range(M):
                for l in range(M):
                    if 0<= i+k < N and 0 <= j+l < N:
                        tmpsum += arr[i+k][j+l]
            maxsum = max(maxsum, tmpsum)

    print(f"#{t} {maxsum}")