T = int(input())

for t in range(1,T+1):
    N = int(input())
    A = [0]*N
    B = [0]*N
    for n in range(N):
        A[n], B[n] = map(int,input().split())
    P = int(input())
    C = []
    for p in range(P):
        C.append(int(input()))

    tmp = [0]*5000

    for i in range(N):
        for j in range(A[i],B[i]+1):
            tmp[j-1] += 1

    print(f"#{t}", end = ' ')
    for c in C:
        print(tmp[c-1], end = ' ')
    print()