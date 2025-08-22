# 중위순회
T = 10


def in_order(T):
    if T:
        in_order(left[T])
        print(string[T], end = '')
        in_order(right[T])

for t in range(1,T+1):
    N = int(input())

    string = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    arr = []
    for i in range(N):
        arr.append(list(input().split()))

    for i in range(N):
        string[i+1] = arr[i][1]

    for i in range(N):
        if len(arr[i]) == 4:
            left[i+1] = int(arr[i][2])
            right[i+1] = int(arr[i][3])
        elif len(arr[i]) == 3:
            left[i+1] = int(arr[i][2])


    print(f"#{t}", end = ' ')
    in_order(1)
    print()
