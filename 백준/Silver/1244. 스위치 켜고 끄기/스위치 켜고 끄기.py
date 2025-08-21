N = int(input())
arr = list(map(int,input().split()))
M = int(input())
for i in range(M):
    gender, switch = map(int,input().split())
    if gender == 1:
        for j in range(switch-1,N,switch):
            if arr[j] == 0:
                arr[j] = 1
            else: arr[j] = 0
    else:
        if arr[switch - 1] == 0:
            arr[switch - 1] = 1
        else: arr[switch -1] = 0

        for j in range(N//2 + 1):
            left = switch -1 -j
            right = switch -1 +j
            if 0 <= left and right < N:
                if arr[left] == arr[right]:
                    if arr[left] == 0: arr[left] = 1
                    elif arr[left] == 1: arr[left] = 0
                    if arr[right] == 0 : arr[right] = 1
                    elif arr[right] == 1: arr[right] = 0
                else:
                    break

# 제출형식 (20개마다 줄바꿈)
for i in range(len(arr)):
    print(arr[i], end = ' ')
    if (i+1) % 20 == 0:
        print()
