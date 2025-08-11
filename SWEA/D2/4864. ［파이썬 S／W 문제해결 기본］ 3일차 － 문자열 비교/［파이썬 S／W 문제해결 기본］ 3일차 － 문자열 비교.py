T = int(input())

def brute_force(p,t):
    i = 0
    j = 0
    M = len(p)
    N = len(t)
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M: return 1
    else: return 0

for t in range(1,T+1):
    str1 = list(input())
    str2 = list(input())
    print(f"#{t}", brute_force(str1,str2))

