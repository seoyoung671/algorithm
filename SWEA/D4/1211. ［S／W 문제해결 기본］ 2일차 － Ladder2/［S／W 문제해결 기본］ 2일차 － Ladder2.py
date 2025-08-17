T = 10

for t in range(1,T+1):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 출발 지점의 인덱스 저장
    start = []
    for i in range(100):
        if arr[0][i] == 1:
            start.append(i)

    # 출발 지점 갯수만큼 리스트 생성 -> 이곳에 거리 계산해서 집어넣고 최솟값 찾기
    result = []



    # 시작 지점마다의 경우 보기
    for i in range(len(start)):
        # 시작지점의 행은 항상 0
        x = 0
        # 시작 지점의 열을 y로 지정
        y = start[i]
        distance = 0
        while x <99:
            if 0 <= y-1 < 100 and arr[x][y-1] == 1:
                while 0 <= y-1 < 100 and arr[x][y-1] == 1:
                    y -= 1
                    distance += 1
                x += 1
                distance += 1
            elif 0 <= y+1 < 100 and arr[x][y+1] == 1:
                while 0 <= y+1 < 100 and arr[x][y+1] == 1:
                    y += 1
                    distance += 1
                x += 1
                distance += 1
            else:
                x += 1
                distance += 1
        result.append(distance)


    for i in range(len(result)):
        if result[i] == min(result):
            idx = i

    print(f"#{t} {start[idx]}")
