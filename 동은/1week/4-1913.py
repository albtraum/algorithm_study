# https://www.acmicpc.net/problem/1913
N = int(input())
target = int(input())
loc_x,loc_y = 0,0
board =[[0]*N for _ in range(N)]

cnt = 2
x,y = (N-1)//2,(N-1)//2 #시작점 
board[x][y] =1
if target ==1:
    loc_x,loc_y = x,y

for i in range(1,N):
    for _ in range(1,i+1):
        #세로축
        if i % 2 == 1:
            x -= 1
        elif i % 2 == 0:
            x += 1
        if cnt == target:
            loc_x,loc_y = x,y
        board[x][y] = cnt
        cnt+=1
        
    for _ in range(1,i+1):
        #가로축
        if i % 2 == 1:
            y += 1
        elif i % 2 == 0:
            y -= 1
        if cnt == target:
            loc_x,loc_y = x,y    
        board[x][y] = cnt
        cnt+=1
        
    if i ==N-1:
        for _ in range(1,i+1):
            x-=1
            if cnt == target:
                loc_x,loc_y = x,y
            board[x][y] = cnt
            cnt+=1
            
for e in board:
    for f in e:
        print(f,end=" ")
    print(" ")
#문제에서 제시한 좌표는 인덱스 + 1 을 의미
print(loc_x+1,loc_y+1)
