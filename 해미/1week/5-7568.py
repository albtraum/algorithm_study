# https://www.acmicpc.net/problem/7568
import sys
N = int(sys.stdin.readline())
a = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    a.append([x, y])

rank = [1] * N #rank에 해당하는 배열 생성
for j in range(N):
    for k in range(N):
        if a[j][0] < a[k][0] and a[j][1] < a[k][1]: #자신의 rank 수 세기
            rank[j] += 1
        elif j == k:
            continue

for b in rank:
    print(b, end=' ')