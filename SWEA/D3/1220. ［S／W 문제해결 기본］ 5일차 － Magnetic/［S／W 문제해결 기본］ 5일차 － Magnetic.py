T = 10

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    for j in range(N):
        tmp = []
        for i in range(N):
            tmp.append(arr[i][j])
        filtered = [x for x in tmp if x!=0] # 0만 빼고 보고싶음

        for i in range(len(filtered)):
            if filtered[i] == 2:
                filtered[i] = 0
            elif filtered[i] == 1:
                break

        for i in range(len(filtered)-1,-1,-1):
            if filtered[i] == 1:
                filtered[i] = 0
            elif filtered[i] == 2:
                break

        filtered = [x for x in filtered if x!=0]
        # 0 빼고, 방해물 없어서 테이블 아래로 떨어진 자성체 빼고 새로운 리스트 만들어짐

        # 열마다 검사
        # 2,1 의 패턴이 발견될때마다 교착이라고 판단 -> result +1
        for i in range(len(filtered)-1):
            if (filtered[i], filtered[i+1]) == (1,2):
                result += 1


    print(f"#{t} {result}")

