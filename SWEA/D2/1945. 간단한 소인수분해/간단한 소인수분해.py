T = int(input())

for t in range(1,T+1):
    N = int(input())

    cnt = [0]*5

    while N != 1:
        if N % 2 == 0:
            cnt[0] += 1
            N //= 2
            continue
        if N % 3 == 0:
            cnt[1] += 1
            N //= 3
            continue
        if N % 5 == 0:
            cnt[2] += 1
            N //= 5
            continue
        if N % 7 == 0:
            cnt[3] += 1
            N //= 7
            continue
        if N % 11 == 0:
            cnt[4] += 1
            N //= 11
            continue
    print(f"#{t}", *cnt)