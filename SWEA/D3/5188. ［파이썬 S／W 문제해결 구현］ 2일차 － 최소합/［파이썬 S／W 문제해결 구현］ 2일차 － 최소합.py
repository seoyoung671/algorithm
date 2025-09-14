
def minsum(total,x,y):
    global result
    if total >= result:
        return

    if x == N-1 and y == N-1:
        result = total
        return

    for i,j in (0,1),(1,0):
        nx, ny = x +i, y+j
        if 0 <= nx < N and 0 <= ny < N:
            minsum(total+arr[nx][ny],nx,ny)



T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 99999999999999

    minsum(arr[0][0],0,0)
    print(f"#{t} {result}")