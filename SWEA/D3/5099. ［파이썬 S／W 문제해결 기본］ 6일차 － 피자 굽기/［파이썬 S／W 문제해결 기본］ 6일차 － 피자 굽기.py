T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    pizza = [] #피자번호 치즈양

    for idx,cheeze in enumerate(arr):
        pizza.append((idx,cheeze))

    oven = []

    # 피자의 인덱스, 치즈양을 화덕에 넣은 초깃값 생성
    for i in range(N):
        oven.append(pizza[i])

    i = 0
    while N + i < M:
        idx, c = oven[0]
        c //= 2
        if c == 0:
            oven.pop(0)
            oven.append(pizza[N+i])
            i += 1
        else:
            again = oven.pop(0)
            oven.append((again[0], c))

    while len(oven) != 1:
        if oven[0][1] == 0:
            oven.pop(0)
        else:
            again = oven.pop(0)
            oven.append((again[0],again[1]//2))

    print(f"#{t} {oven[0][0]+1}")
