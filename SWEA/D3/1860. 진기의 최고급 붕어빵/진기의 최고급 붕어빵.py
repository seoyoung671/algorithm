T = int(input())

for t in range(1,T+1):
    N, M, K = map(int,input().split())
    arr = list(map(int,input().split()))

    # 붕어 개수를 초마다 카운트
    bungeo = [0] * (max(arr)+1)
    # 손님을 초마다 카운트
    tmp = [0] * (max(arr) + 1)
    total = 0
    for i in range(len(arr)):
        tmp[arr[i]] += 1

    for i in range(M,len(bungeo),M):
        bungeo[i] += K

    for i in range(len(bungeo)):
        total += bungeo[i]
        total -= tmp[i]
        if total < 0:
            print(f"#{t} Impossible")
            break
    if total >= 0:
        print(f"#{t} Possible")