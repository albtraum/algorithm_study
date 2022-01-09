import sys

n, m = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

stack = []
visit = []
count = 0
for i in range(1, n+1):
    if i not in visit:
        stack.append(i)
        while stack:
            node = stack.pop()
            if node not in visit:
                visit.append(node)
                stack.extend(sorted(graph[node]))
        count += 1

print(count)
