def minsum(x,y,summation):
    global result
    if summation >= result:
        return

    if x == N-1 and y == N-1:
        result = min(result,summation)
        return

    for dx,dy in (0,1),(1,0):
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            minsum(nx,ny,summation + arr[nx][ny])


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 9999999999999999
    minsum(0,0,arr[0][0])
    print(f"#{t} {result}")