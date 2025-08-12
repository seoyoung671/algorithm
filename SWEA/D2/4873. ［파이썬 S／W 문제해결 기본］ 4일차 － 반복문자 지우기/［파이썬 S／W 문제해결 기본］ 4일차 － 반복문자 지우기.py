T = int(input())

for t in range(1,T+1):
    txt = input()

    top = -1
    stack = [0]*1000
    ans = 1

    for x in txt:
        top += 1
        stack[top] = x
        if stack[top] == stack[top-1]:
            stack[top] = 0
            stack[top-1] = 0
            top -= 2
    cnt = 0
    for i in range(len(stack)):
        if stack[i] != 0:
            cnt += 1
        else: break
    print(f"#{t} {cnt}")