n = int(input())
m = int(input())
mat = [[0]*n for i in range(n)]
visited = [0 for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    mat[a-1][b-1] = 1
    mat[b-1][a-1] = 1
def dfs(v):
  visited[v] = 1
  for i in range(n):
    if mat[v][i] == 1 and visited[i] == 0:
      dfs(i)
dfs(0)
cnt = 0
for i in range(1, n):
  if visited[i] == 1:
    cnt += 1
print(cnt)