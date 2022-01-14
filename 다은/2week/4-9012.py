import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    ps = list(input().strip())
    while ps:
        stack.append(ps.pop(0))
        if len(stack) >= 2:
            # stack에 ()로 쌓였으면
            if stack[-1] == ')' and stack[-2] == '(':
                # (, )를 제거
                stack.pop()
                stack.pop()
    if stack:
        # 스택에 값이 남음 -> VPS가 아님
        print("NO")
    else:
        # 스택이 비었음 -> VPS
        print("YES")
