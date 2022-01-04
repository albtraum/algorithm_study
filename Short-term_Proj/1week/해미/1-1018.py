# https://www.acmicpc.net/problem/1018
import sys
N, M = map(int, input().split())
maps =  [list(input()) for _ in range(N)] #체스판 입력받기 
# 문제에서 B로 시작하는 체스판과 W로 시작하는 체스판 구별하라고 함
ans = 64
black = []
white = []
for i in range(8):
    if i % 2 == 0:
        black.append(list(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']))
        white.append(list(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']))
    else:
        white.append(list(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']))
        black.append(list(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']))

for i in range(0, N-7, 1): #체스판의 갯수 찾기
    for j in range(0, M-7, 1): #체스판의 갯수 찾기 (전체 체스판 8*8로 잘라서 몇개가 나오는지 구함)
        whiteNum = 0
        blackNum = 0
        for k in range(i, i + 8): # black로 시작하는 체스판과 비교하여 cnt 세기
            for s in range(j, j + 8):
                if black[k-i][s-j] != maps[k][s]:
                    blackNum += 1
        for k in range(i, i + 8): # white로 시작하는 체스판과 비교하여 cnt세기
            for s in range(j, j + 8):
                if white[k-i][s-j] != maps[k][s]:
                    whiteNum += 1
        ans = min(ans, min(blackNum, whiteNum)) # black을 바꿀지 white 를 바꿀지 정함
print(ans)