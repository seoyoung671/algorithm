T = int(input())

def sunyeol(cnt):
    global sum,sumlist
    if cnt == N-1:
        tmp= [0,*path,0] # 가능한 모든 경로
        for i in range(len(tmp)-1):
            sum += arr[tmp[i]][tmp[i+1]]
        sumlist.append(sum)
        sum = 0
        return

    for i in range(1,N):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        sunyeol(cnt + 1)
        path.pop()
        used[i] = False


for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0]*N
    path = []
    sum = 0
    sumlist = []
    sunyeol(0)
    print(f"#{t} {min(sumlist)}")
