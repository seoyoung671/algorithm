T = 10

for t in range(1,T+1):
    tc = int(input())
    arr = list(map(int,input().split()))

    while 0 not in arr:
        for num in range(1,6):
            item = arr.pop(0)
            if (item - num) > 0:
                arr.append(item-num)
            else:
                arr.append(0)
                break

    print(f"#{tc}",*arr)