T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N-1):
        for j in range(i+1,N):
            # 두 개씩 비교
            # 시작1 > 시작2 + 끝1 < 끝2 인 경우
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
            # 시작1 < 시작2 + 끝1 > 끝2 인 경우
            elif arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                cnt += 1

    print(f"#{t} {cnt}")