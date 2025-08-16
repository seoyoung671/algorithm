T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    tmp = [0]*(N)

    for i in range(len(arr)):
        tmp[arr[i]-1] += 1

    result = []
    for i in range(len(tmp)):
        if tmp[i] == 0:
            result.append(i+1)

    print(f"#{t}", *result)