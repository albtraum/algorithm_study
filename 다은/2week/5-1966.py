import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # enumerate를 사용해 index 값과 중요도 함께 저장
    queue = list(enumerate(map(int, input().split())))
    deq = deque(queue)
    cnt = 0
    state = 1
    while state:
        # 맨 앞의 문서의 중요도보다 중요도가 큰 값이 존재한다면
        if deq[0][1] < max(deq, key=lambda x: x[1])[1]:
            # 맨 앞의 문서를 제일 뒤로
            deq.append(deq.popleft())
        else:
            # 맨 앞의 중요도보다 큰 중요도가 존재하지 않는다면
            # 몇 번째로 인쇄되었는지 궁금한 문서라면
            if deq[0][0] == m:
                # 반복문 종료 -> 현재 문서의 인쇄 순서만 알면 됨
                state = 0
            # 몇 번째로 인쇄되었는지 궁금한 문서가 아니라면
            deq.popleft()
            cnt += 1
    print(cnt)
