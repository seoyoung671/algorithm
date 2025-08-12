T = 10
for t in range(1,T+1):
    num, number = input().split()

    stack = []

    for n in number:
        stack.append(n)
        length = len(stack)
        if 2 <= length:
            if stack[length-1] == stack[length-2]:
                stack.pop(length-1)
                stack.pop(length-2)
    print(f"#{t}",''.join(stack))