T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)

    cnt = 0
    while weight and truck: # weight와 truck 에 요소가 모두 존재하는 경우에만 순회
        # 만약 첫번째 weight 값이 첫번째 truck 값보다 크다면 pop
        if weight[0] > truck[0]:
            weight.pop(0)
        # 그게 아니라면, 첫번째 truck과 첫번째 weight을 pair(동시에 pop). cnt에 +1
        else:
            cnt += weight[0]
            weight.pop(0)
            truck.pop(0)

    print(f"#{t} {cnt}")