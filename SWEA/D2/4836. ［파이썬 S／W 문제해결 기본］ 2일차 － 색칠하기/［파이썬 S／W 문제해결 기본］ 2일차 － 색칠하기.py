T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    tmp = [[0]*10 for _ in range(10)]

    for i in range(N):
        for row in range(arr[i][0],arr[i][2]+1):
            for col in range(arr[i][1],arr[i][3]+1):
                tmp[row][col] += arr[i][4]

    cnt = 0
    for i in range(10):
        for j in range(10):
            if tmp[i][j] == 3:
                cnt += 1
    print(f"#{t} {cnt}")