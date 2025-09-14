T = int(input())

def janghun(length,start):
    global result
    if length >= B:
        result = min(length,result)
        return

    if start == N:
        return

    if length + arr[start] < result:
        janghun(length+arr[start],start+1)

    janghun(length, start+1)

for t in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))

    path = []
    result = 999999999999

    janghun(0,0)
    print(f"#{t} {result-B}")