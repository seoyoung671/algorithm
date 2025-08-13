T = int(input())

for t in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    # 문제가 있을 때마다 result에 1을 추가 (초기화)
    result = 0

    # 행의 경우
    for i in range(9):
        tmp = sorted(arr[i])
        if [1,2,3,4,5,6,7,8,9] != tmp:
            result += 1


    # 열의 경우
    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(arr[j][i])
        tmp.sort()
        if [1,2,3,4,5,6,7,8,9] != tmp:
            result += 1


    # 3x3의 경우
    for i in range(0,9,3):
        for j in range(0,9,3):
            tmp = []
            for k in range(3):
                for l in range(3):
                    tmp.append(arr[i+k][j+l])
            tmp.sort()
            if [1,2,3,4,5,6,7,8,9] != tmp:
                result += 1

    ans = 0

    if result >= 1:
        ans = 0
    else: ans = 1
    print(f"#{t} {ans}")
