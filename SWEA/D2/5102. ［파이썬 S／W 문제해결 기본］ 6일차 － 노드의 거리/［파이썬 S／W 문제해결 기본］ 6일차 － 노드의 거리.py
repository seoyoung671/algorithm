T = int(input())

def bfs_find(start, end, V):
    visited = [0] * (V+1)
    q = []

    visited[start] = 1
    q.append(start)

    while q:
        current_node = q.pop(0)
        for next_node in adj_list[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[current_node] + 1
                q.append(next_node)
    if visited[start] == 0  or visited[end] == 0:
        return 0
    else: return abs(visited[end] - visited[start])

for t in range(1,T+1):
    V, E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())

    adj_list = [[] for _ in range(V+1)]
    for i in range(E):
        adj_list[arr[i][0]].append(arr[i][1])
        adj_list[arr[i][1]].append(arr[i][0])


    result = bfs_find(S,G,V)
    print(f"#{t} {result}")
