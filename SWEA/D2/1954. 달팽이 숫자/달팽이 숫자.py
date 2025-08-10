T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    x,y = 0,0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    direction = 0

    for i in range(1,N*N+1):
        arr[x][y] = i
        nx, ny = x + dx[direction], y + dy[direction]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]
        x,y = nx, ny

    print(f"#{t}")
    for row in arr: print(*row)
