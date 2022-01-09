#idea
#1. 벽을 3개 치는 경우구하기
#2. 벽을 쳐보고 바이러스 퍼뜨리고 0의 개수구하기(모든 경우 반복?)
#####못 푼 문제(다른 코드참고해서 풀었습니다.)#####
##########다시 해보기##########
import sys
from itertools import combinations
from copy import deepcopy

input=sys.stdin.readline
N,M=map(int,input().split())
mat=[[0]*M for _ in range(N)]

safe=[]
virus=[]
maxSafe=0

for i in range(N):
  row=list(map(int,input().split()))
  for j in range(M):
    mat[i][j]=row[j]
    if row[j]==0:
      maxSafe+=1
      safe.append((i, j))
    elif row[j]==2:
      virus.append((i, j))

maxSafe-=3
ans=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

for positions in combinations(safe,3):
  cnt_trans=0
  temp_mat=deepcopy(mat)
  for pos in positions:
    row,col=pos
    temp_mat[row][col]=1    
  stack=deepcopy(virus)
  while stack:
    curR,curC=stack.pop()
    for i in range(4):
      if 0<=curR+dy[i]<N and 0<=curC+dx[i]<M and temp_mat[curR+dy[i]][curC+dx[i]]==0:
        temp_mat[curR+dy[i]][curC+dx[i]] = 2
        cnt_trans += 1
        stack.append((curR+dy[i], curC+dx[i]))
  if ans<maxSafe-cnt_trans:
    ans=maxSafe-cnt_trans
print(ans)
