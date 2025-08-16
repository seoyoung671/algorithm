T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    maxresult = 0

    for i in range(N):
        for j in range(i+1,N):
            tmp = arr[i] * arr[j]

            tmplist = []

            for k in str(tmp):
                tmplist.append(int(k))

            if len(tmplist) > 1:
                for k in range(len(tmplist)-1):
                        if tmplist[k] > tmplist[k+1]:
                            break
                else: maxresult = max(maxresult, tmp)
            elif len(tmplist) == 1:
                maxresult = max(maxresult, tmp)
    if maxresult > 0 :
        print(f"#{t} {maxresult}")
    else: print(f"#{t} -1")