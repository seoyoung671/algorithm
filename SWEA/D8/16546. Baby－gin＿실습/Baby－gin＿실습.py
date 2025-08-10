T = int(input())

for t in range(1,T+1):
    arr = list(map(int,input().strip()))

    cnt = [0]*12

    for i in arr:
        cnt[i] += 1

    tri = run1 = 0

    i = 0
    while i < 10 :
        if cnt[i] >= 3:
            cnt[i] -= 3
            tri += 1
            continue
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            run1 += 1
            continue
        i += 1

    if tri+run1 == 2: print(f"#{t} true")
    else: print(f"#{t} false")