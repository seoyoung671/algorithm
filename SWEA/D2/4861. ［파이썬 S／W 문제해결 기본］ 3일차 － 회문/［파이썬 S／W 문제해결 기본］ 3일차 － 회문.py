T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    # 탐색의 편의를 위해 각 알파벳을 요소로 갖는 리스트로 받음

    # 가로의 경우
    for i in range(N):
        for j in range(N-M+1):
            tmp = ''
            for k in range(j,M+j):
                tmp = tmp + (arr[i][k])
            reverse = tmp[::-1]
            if tmp == reverse:
                print(f"#{t} {tmp}")

    # 세로의 경우
    for i in range(N):
        for j in range(N-M+1):
            tmp = ''
            for k in range(j,M+j):
                tmp = tmp + (arr[k][i])
            reverse = tmp[::-1]
            if tmp == reverse:
                print(f"#{t} {tmp}")
