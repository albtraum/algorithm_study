# https://www.acmicpc.net/problem/10773
import sys
K = int(input())
stack = []
for _ in range(K):
    num = int(sys.stdin.readline())
    #0나오면 가장 최근에 쓴 수 지움
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
