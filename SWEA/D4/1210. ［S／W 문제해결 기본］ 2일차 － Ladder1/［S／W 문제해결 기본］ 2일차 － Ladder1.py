T = 10

for t in range(1,T+1):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    # x의 초깃값 지정
    x = 99

    for i in range(100):
        if arr[x][i] == 2:
            y = i


    # 시작값을 찾음. 현위치 x, y
    while x != 0:
        if 0 <= y + 1 < 100 and arr[x][y+1] == 1:
            while  0 <= y + 1 < 100 and arr[x][y+1] == 1:
                y += 1
            x -= 1
        elif 0 <= y-1 < 100 and arr[x][y-1] == 1:
            while 0 <= y-1 < 100 and arr[x][y-1] == 1:
                y -= 1
            x -= 1
        else: x -= 1

    print(f"#{t} {y}")