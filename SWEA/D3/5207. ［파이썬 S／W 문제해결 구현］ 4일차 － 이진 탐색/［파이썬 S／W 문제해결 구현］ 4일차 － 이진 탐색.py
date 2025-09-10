
def constrained_binary_search(a, x):
    l, r = 0, len(a) - 1
    last_dir = 0
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return True
        elif x < a[m]:
            if last_dir == -1:     # 직전에도 왼쪽으로 갔으면 실패
                return False
            r = m - 1
            last_dir = -1
        else:  # x > a[m]
            if last_dir == 1:      # 직전에도 오른쪽으로 갔으면 실패
                return False
            l = m + 1
            last_dir = 1
    return False

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(2)]
    result = 0
    arr1 = sorted(arr[0])
    for i in range(M):
        result += constrained_binary_search(arr1,arr[1][i])
    print(f"#{t} {result}")