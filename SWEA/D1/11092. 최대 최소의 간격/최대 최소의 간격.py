T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    # max 값 구하기
    maxvalue = 0
    for i in range(N):
        if maxvalue <= arr[i]:
            maxvalue = arr[i]
            maxidx = i

    minvalue = 101
    for i in range(N):
        if minvalue > arr[i]:
            minvalue = arr[i]
            minidx = i

    print(f"#{t} {abs(maxidx - minidx)}")