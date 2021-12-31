from collections import deque
N,K = map(int,input().split())
arr=deque()
p=[]
for i in range(1,N+1):
  arr.append(i)
for i in range(N):
  for j in range(K):
    arr.append(arr.popleft())
  p.append(arr.pop())
print("<",end="")
for i in range(N-1):
  print(p[i],end=", ")
print(p[-1],end="")
print(">")