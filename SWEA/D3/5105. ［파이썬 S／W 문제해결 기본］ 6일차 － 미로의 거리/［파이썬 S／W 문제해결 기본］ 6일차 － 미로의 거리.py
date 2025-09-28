T = int(input())

def bfs(N,maze,start):
    # 시작점 
    x, y = start[0],start[1]
    queue = [(x,y,0)]
    
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    front = 0
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while front < len(queue):
        x,y,dist = queue[front]
        front += 1
        
        for d in range(4):
            nx,ny = x + dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if maze[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny,dist+1))
                elif maze[nx][ny] == 3:
                    return dist
             

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().strip())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i,j]
	
    answer = bfs(N,arr,start)
    if answer == None:
        answer = 0
    print(f"#{t} {answer}")
    
    