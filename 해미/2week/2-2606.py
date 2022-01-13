import sys
from collections import deque
N = int(input())
M = int(input())
graph = [[] for _ in range(1 + N)]
visited = [0]*(1 + N)
 
for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
 
def bfs(graph, visited, start):
  global count
  q = deque([start])
  visited[start] = True
  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        count += 1
 
count = 0
bfs(graph, visited, 1)
print(count)