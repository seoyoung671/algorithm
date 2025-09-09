def findcandy(A,B,C):
    if A < 1 or B < 2 or C < 3: # A,B,C 상자의 최솟값은 각각 1,2,3이다
        return -1
    elif A < B and B < C: # A<B<C이면 먹어야되는 사탕의 수가 0개
        return 0
    else: # 두 경우에 해당하지 않으면 우선 1 출력
        return 1

T = int(input())

for t in range(1,T+1):
    A,B,C = map(int,input().split())

    if findcandy(A,B,C) == 1:
        cnt = 0
        while A >= B or B >= C: # B가 A보다 작거나, C가 B보다 작은 경우
            if A >= B:
                cnt += (A-B+1) # A와 B의 차이에 1개 더 먹어야 경우 만족됨
                A = B-1
                continue
            if B >= C:
                cnt += (B-C+1) # B와 C의 경우도 마찬가지임
                B = C-1
        print(f"#{t} {cnt}")
    elif findcandy(A,B,C) == 0:
        print(f"#{t} 0")
    else: print(f"#{t} -1")
