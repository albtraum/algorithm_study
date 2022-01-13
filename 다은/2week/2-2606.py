import sys
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())

graph = [[] for _ in range(n+1)]

# 그래프
for _ in range(k):
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

stack = []
visit = []
stack.append(1)

# DFS
while stack:
    node = stack.pop()
    # 중복된 방문이 아니라면
    if node not in visit:
        visit.append(node)
        stack.extend(graph[node])

# 1번과 연결된 컴퓨터 개수(-1은 1번 컴퓨터 자신)
print(len(visit)-1)
