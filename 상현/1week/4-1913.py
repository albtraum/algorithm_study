#arr[0][0]=n*n
#아래로 n-1 오른쪽으로 n-1 위로 n-1 왼쪽으로 n-2 아래로 n-2 
#########이게 왜 런타임에러야ㅑㅑㅑㅑㅑㅑㅑㅑㅑㅑㅑㅑㅑㅑㅑㅑ
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
board=[[0 for _ in range(n)] for _ in range(n)]

dx=[-1,0,1,0]  #좌우
dy=[0,-1,0,1]  #상하
x=y=0
start=0
num=n**2
len=n-1
board[y][x]=num
# 0->3  1->2 2->1 3->0
while True:
  if start==0:
    for i in range(3):
      for _ in range(len):
        y+=dy[3-i]
        x+=dx[3-i]
        num-=1
        board[y][x]=num
        if num==m:
          ans=[y+1,x+1]
    start=1
    len-=1
  else:
    #좌하우상반복
    for i in range(4):
      if i==2:
          len-=1
      for _ in range(len):
        #0->0 1->3 2->2 3->1
        y+=dy[(4-i)%4]
        x+=dx[(4-i)%4]
        num-=1
        board[y][x]=num
        if num==m:
          ans=[y+1,x+1]
    len-=1
    if board[n//2][n//2]!=0:
      break
    
for i in range(n):
    print(*board[i])
print(*ans)

