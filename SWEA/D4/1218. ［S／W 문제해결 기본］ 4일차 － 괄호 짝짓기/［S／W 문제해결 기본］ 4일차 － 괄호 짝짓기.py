T = 10
for t in range(1,T+1):
    N = int(input())
    txt = input()

    mydict = {')': '(', '}':'{', ']':'[','>':'<' }

    top = -1
    stack = [0] * N
    result = 1

    for x in txt:
        if x in ('(','{','[','<'):
            top += 1
            stack[top] = x
        elif x in (')','}','>',']'):
            if stack[top] != mydict[x]:
                result = 0
                break
            else:
                top -= 1
    print(f"#{t} {result}")
