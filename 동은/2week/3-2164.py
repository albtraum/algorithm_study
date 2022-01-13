# https://www.acmicpc.net/problem/2164
from collections import deque
N = int(input())

que = deque()
for i in range(N,0,-1):
    que.append(i)

#로테이트로 하나씩 미룸
while(len(que) != 0 ):
    ans = que.pop()
    que.rotate(1)
print(ans)
