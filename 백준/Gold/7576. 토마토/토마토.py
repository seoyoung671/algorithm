from collections import deque

# M행 N열
M, N  = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 처음부터 익어있는 토마토. = 시작값
tmt = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tmt.append([i,j])

# 익지 않은 토마토가 없다면 0을 출력하고 종료
def check_for_zero(arr):
    for row in arr:
        if 0 in row:
            return False
    return True

if check_for_zero(arr) == True:
    print(0)
    exit()

def bfs(tmt,N,M):
    visited = [[0]*M for _ in range(N)]
    q = deque(tmt)
    for i,j in tmt:
        visited[i][j] = 1
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi,wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < M and visited[wi][wj] == 0 and arr[wi][wj] == 0:
                q.append([wi,wj])
                visited[wi][wj] = visited[ti][tj] + 1
                # arr[wi][wj] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:
                return -1
    else:
        return max(map(max,visited)) - 1

print(bfs(tmt,N,M))