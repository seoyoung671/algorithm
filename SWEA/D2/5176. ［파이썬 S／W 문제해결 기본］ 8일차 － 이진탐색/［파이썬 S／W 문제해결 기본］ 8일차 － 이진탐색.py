# 중위순회
T = int(input())
def in_order(node):
    global cnt
    if node <= N:
        in_order(node*2)
        tree[node] = cnt
        cnt += 1
        in_order(node*2+1)

for t in range(1,T+1):
    # N개의 노드를 가진 완전 이진 트리 만들기
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    in_order(1)
    print(f"#{t} {tree[1]} {tree[N//2]}")
