T = int(input())

for t in range(1,T+1):
    txt = input()

    ans = 1
    top = -1
    stack = [0] * 100

    # 소괄호, 중괄호, 대괄호 모두 포함된 리스트 생성
    mylist = ['(', ')', '{', '}', '[', ']']

    # txt의 문자 하나씩 순회
    for x in txt:
        # x가 열리는 괄호라면
        if x in ('[','{','('):
            # top에 1 추가
            top += 1
            # stack[top]에 x를 저장
            stack[top] = x
        # x가 닫히는 괄호라면 경우를 세 개로 나눔
        elif x in (']','}',')'):
            # top이 -1, 즉 아무것도 없는 상태라면 ans는 0, break
            if top == -1:
                ans = 0
                break
            # top에 있는 요소가 리스트에서 자기 옆에 있는 요소 (즉 짝이 되는 괄호) 이면 pop
            elif stack[top] == mylist[mylist.index(x)-1]:
                top -= 1
            # 짝이 되는 괄호가 아니고, 아무것도 없는 상태가 아니라면 짝이 아닌 괄호
            # 즉 이땐 짝은 아닌 괄호가 입력된 상황
            else:
                ans = 0
                break

    # top이 -1이 아니라면(모두 pop된 상태가 아니라면) ans는 0
    if top != -1:
        ans = 0
    print(f"#{t} {ans}")