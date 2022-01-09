# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
def dfs(graph, v, visited):
    visited[v] = True  
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
#재귀로 탐색

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v= queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

node_N, edge_M, start_V = map(int,sys.stdin.readline().split())

graph=[
    [] for _ in range(node_N+1)
]


for _ in range(edge_M):
    temp=list(map(int,sys.stdin.readline().split()))
    #양방향
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

#작은 수 방문
for e in graph:
    e.sort()


#미방문 노드 
visited = [False] * (node_N+1)

dfs(graph,start_V,visited)
print("")
visited = [False] * (node_N+1)
bfs(graph,start_V,visited)
