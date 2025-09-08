T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int,input().split()))

    # 도착 시간 기준으로 정렬해서 구하고자 함
    # arr의 두 번째 값 기준으로 버블정렬
    for i in range(N-1):
        for j in range(N-1-i):
            if arr[j][1] > arr[j+1][1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    # 처음 값은 무조건 싣는게 유리
    cnt = 1
    # 현재 요소의 종료시간이 다음 요소의 시작시간보다 작거나 같다면 다음 요소를 넣음
    while len(arr) != 1:
        if arr[0][1] <= arr[1][0]:
            cnt += 1
            arr.pop(0)
        else:
            arr.pop(1)

    print(f"#{t} {cnt}")