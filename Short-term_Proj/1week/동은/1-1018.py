# https://www.acmicpc.net/problem/1018
import sys
from typing import Mapping

f=open('short_1week\\test.txt')

#N,M = map(int,input().split())
N,M = map(int,f.readline().split())
#M은 가로, N은 세로 
ans = 65
board = []
for _ in range(N):
    #board.append(sys.stdin.readline().rstrip())
    board.append(f.readline().rstrip())
#sliding window 8*8

#case 1 : B로 시작하는 경우의 비교용 보드판
case_1,case_2 = [],[]
cnt = 0 
for i in range(N):
    temp_1 =""
    temp_2 =""
    for j in range(M):
        if cnt%2 == 0 :
            temp_1 +="B"
            temp_2 +="W"
        else:
            temp_1 +="W"
            temp_2 +="B"
        cnt +=1
    if(M%2==0):
        cnt+=1
    case_1.append(temp_1)
    case_2.append(temp_2)
#case 2 : W로 시작하는 경우의 비교용 보드판 

#compare 
# 테스트 케이스별 비교 후 최솟값을 ans으로 출력
# 8*8크기의 행렬이 스캔하는 방식 

for y in range(N-7):
    for x in range(M-7):
        temp_1 = 0
        temp_2 = 0
        for i in range(8):
            for j in range(8):
                if board[i+y][j+x] != case_1[i][j]:
                    temp_1+=1
                if board[i+y][j+x] != case_2[i][j]:
                    temp_2+=1
        ans = min(ans,temp_1,temp_2)
                
print(ans)
