def bfs(si,sj):
    visited = [[0]*16 for _ in range(16)]
    q = [[si,sj]]
    visited[si][sj] = 1

    while q:
        ti,tj = q.pop(0)
        if arr[ti][tj] == 3:
            return 1
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi,wj = ti + di, tj + dj
            if 0 <= wi < 16 and 0 <= wj < 16 and arr[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi,wj])
                visited[wi][wj] = visited[ti][tj] + 1
    if arr[ti][tj] != 3:
        return 0



T = 10
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si,sj = i, j

    print(f"#{t} {bfs(si,sj)}")