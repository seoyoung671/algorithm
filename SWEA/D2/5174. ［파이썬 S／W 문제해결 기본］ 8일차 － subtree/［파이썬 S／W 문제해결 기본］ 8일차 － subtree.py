T = int(input())

for t in range(1,T+1):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))

    # 노드 번호는 1번부터 E+1번까지 존재
    left = [0] * (E +2)
    right = [0] * (E +2)
    par = [0] * (E +2)

    for i in range(E):
        p,c = arr[i*2], arr[i*2+1]
        par[c] = p

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c


    cnt = 0
    def pre_order(T):
        global cnt
        if T:
            cnt += 1
            pre_order(left[T])
            pre_order(right[T])
        return cnt

    print(f"#{t} {pre_order(N)}")