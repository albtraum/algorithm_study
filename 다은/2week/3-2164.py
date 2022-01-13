import sys
from collections import deque

n = int(sys.stdin.readline().strip())

# 1~n 까지 카드
queue = [i for i in range(1, n+1)]
deq = deque(queue)
while len(deq) != 1:
    # 제일 위 카드를 버린다
    deq.popleft()
    # 그 다음, 제일 위 카드를 맨 아래로 옮긴다
    deq.append(deq.popleft())


print(deq[0])
