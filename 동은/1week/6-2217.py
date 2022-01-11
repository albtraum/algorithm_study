# https://www.acmicpc.net/problem/2217
import sys
N = int (input())
line = []
weight = []
for _ in range(1,N+1):
    line.append( int((sys.stdin.readline().rstrip())))
line.sort(reverse=True) 
cnt = 1
for e in line:
    weight.append(e*cnt)
    cnt +=1
print(max(weight))

# 무게를 가장 많이 드는 것이 목적 
# 로프 드는 무게가 낮은 쪽이 기준이 되므로, 이걸로 확인 
