# https://www.acmicpc.net/problem/2606
import sys
global cnt
cnt = 0
def dfs(graph, start,v_list):
    v_list[start] = True
    for i in graph[start]:
        if not v_list[i]:
            dfs(graph, i ,v_list)
    global cnt 
    #감염 카운트
    cnt += 1
com_num = int(input())
line_num = int(input())
v_list = [False] * (com_num+1)

graph=[
    [] for _ in range(com_num+1)
]
for _ in range(line_num):
    temp=list(map(int,sys.stdin.readline().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

for e in graph:
    e.sort()

dfs(graph, 1 ,v_list)
print(cnt-1)
