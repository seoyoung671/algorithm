T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    startlist = [(0,0)]
    for x in range(N):
        for y in range(N):
            # 인덱스 범위를 벗어나지 않고, 좌상 값이 0이며 현재 값은 0 이 아닌 지점
            if 0 <= x-1 < N and 0 <= y-1 < N and arr[x-1][y] == 0 and arr[x][y-1] == 0 and arr[x][y] != 0:
                startlist.append((x,y))
            # x값이 0이어서 왼쪽에 값이 없고, 위쪽 값은 0이며 현재 값은 0이 아닌 지점
            elif x == 0 and 0 <= y-1 < N and arr[x][y-1] == 0 and arr[x][y] != 0:
                startlist.append((x,y))
            # y값이 0이어서 위쪽에 값이 없고, 왼쪽 값은 0이며 현재 값은 0이 아닌 지점
            elif y == 0 and 0 <= x-1 < N and arr[x-1][y] == 0 and arr[x][y] != 0:
                startlist.append((x,y))
    # 행렬의 시작점만 모아놓은 리스트 생성됨

    # 행렬의 갯수 = startlist의 길이
    matrixcnt = len(startlist)

    # 행렬의 크기를 저장할 리스트 생성
    matrixsize = []
    for x,y in startlist:
        row, col = 1,1
        while arr[x][y] != 0:
            x += 1
            row += 1
        # 인덱스 벗어난 범위까지 포함되어서 인위적으로 -1 해줌
        x -= 1
        row -= 1
        while arr[x][y] != 0:
            y += 1
            col += 1
        y -= 1
        col -= 1
        matrixsize.append((row,col))

    # 행,열 정보를 기록한 리스트 형성

    # 행렬 크기 계산해서 차례로 정렬
    for i in range(len(matrixsize)-1):
        for j in range(i+1,len(matrixsize)):
            if matrixsize[i][0]*matrixsize[i][1] > matrixsize[j][0]*matrixsize[j][1]:
                matrixsize[i], matrixsize[j] = matrixsize[j], matrixsize[i]

            elif matrixsize[i][0]*matrixsize[i][1] == matrixsize[j][0]*matrixsize[j][1]:
                if matrixsize[i][0] > matrixsize[j][0]:
                    matrixsize[i], matrixsize[j] = matrixsize[j], matrixsize[i]

    print(f"#{t} {matrixcnt}", end = ' ')
    for i in range(len(matrixsize)):
        print(*matrixsize[i],end = ' ')
    print()
