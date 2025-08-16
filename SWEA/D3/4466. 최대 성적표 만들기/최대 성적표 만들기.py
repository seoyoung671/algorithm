T = int(input())

for t in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort(reverse= True)
    ans = 0

    for i in range(K):
        ans += arr[i]

    print(f"#{t} {ans}")