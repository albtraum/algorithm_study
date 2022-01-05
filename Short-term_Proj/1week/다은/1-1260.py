import sys

def dfs(graph, start):
    visit = []
    queue = []
    queue.append(start)

    while queue:
        node = queue.pop()
        if node not in visit:
            visit.append(node)
            queue.extend(sorted(graph[node], reverse=True))

    return visit


def bfs(graph, start):
    visit = []
    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(sorted(graph[node]))

    return visit

n, m, v = map(int, sys.stdin.readline().strip().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in dfs(graph, v):
    print(i, end=" ")
print()
for i in bfs(graph, v):
    print(i, end=" ")
