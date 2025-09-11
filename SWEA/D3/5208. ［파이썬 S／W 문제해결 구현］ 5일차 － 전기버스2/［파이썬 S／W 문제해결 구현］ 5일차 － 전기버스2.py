def dfs(pos,fuel,cnt):
    global best,N
    # cnt가 최소값보다 커진다면 중단 (가지치기)
    if cnt >= best: return
    # 현재 배터리로 종점까지 갈 수 있다면 갱신  
    if pos + fuel >= N - 1 :
        best = cnt
        return
    # 다음 정류장 탐색 (뒤에서부터)
    for step in range(fuel,0,-1):
        nxt = pos + step
        dfs(nxt, arr[nxt],cnt+1)



T = int(input())
for t in range(1,T+1):
    data = list(map(int,input().split()))
    N, arr = data[0],data[1:]
    best = N
    dfs(0,arr[0],0)

    print(f"#{t} {best}")