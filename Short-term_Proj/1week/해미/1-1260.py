# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

def dfs(n): #DFS구현
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n): #BFS구현
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for i in range(m): #리스트 만들기
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for j in range(1, n+1): #리스트 정렬하기
    graph[j].sort()

dfs(v)
visited = [0] * (n + 1)
print()
bfs(v)