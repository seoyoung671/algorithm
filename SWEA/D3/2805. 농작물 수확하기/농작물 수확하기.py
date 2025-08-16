T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    x = N // 2

    result = 0
    l = 0

    for y in range(N):
        result += arr[x][y]
        for j in range(1,l+1):
            for dx in 1,-1:
                nx= x + dx*j
                result += arr[nx][y]
        l += 1
        if y >= N//2:
            l -= 2
    print(f"#{t} {result}")