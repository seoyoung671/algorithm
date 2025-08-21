from collections import deque

# M: 가로(열), N: 세로(행)
M, N  = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 시작점(익은 토마토)과 익지 않은 토마토 개수 파악
q = deque()
unripe_tomatoes = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            # BFS 시작점을 큐에 미리 넣어둡니다. (날짜도 함께 저장하면 편합니다)
            q.append((i,j))
        elif arr[i][j] == 0:
            unripe_tomatoes += 1

# --- 핵심 수정 부분 ---
# 1. 처음부터 익어야 할 토마토가 없다면 0을 출력
if unripe_tomatoes == 0:
    print(0)
else:
    # --- BFS 로직 수정 ---
    # visited 배열 대신 arr 자체를 수정하며 날짜를 기록하면 더 효율적입니다.
    
    # 마지막 날짜를 저장할 변수
    days = 0

    while q:
        ti, tj = q.popleft()
        
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti + di, tj + dj
            
            # 범위 내에 있고, 익지 않은 토마토라면
            if 0 <= wi < N and 0 <= wj < M and arr[wi][wj] == 0:
                # 이전 토마토의 날짜 + 1을 기록
                arr[wi][wj] = arr[ti][tj] + 1
                q.append((wi, wj))
                days = max(days, arr[wi][wj]) # 최대 날짜 갱신

    # 2. 모든 BFS가 끝난 후에도 익지 않은 토마토가 있는지 확인
    still_unripe = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                still_unripe = True
                break
        if still_unripe:
            break

    if still_unripe:
        print(-1)
    # 처음 익은 토마토의 값이 1이었으므로, 최종 결과에서 1을 빼줍니다.
    else:
        print(days - 1 if days > 0 else 0)