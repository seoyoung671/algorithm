T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            tmp = ''
            for k in range(M):
                tmp = tmp + arr[i][j+k]
            reverse = tmp[::-1]
            if tmp == reverse:
                print(f"#{t} {tmp}")

    for j in range(N):
        for i in range(N-M+1):
            tmp = ''
            for k in range(M):
                tmp = tmp + arr[i+k][j]
            reverse = tmp[::-1]
            if tmp == reverse:
                print(f"#{t} {tmp}")