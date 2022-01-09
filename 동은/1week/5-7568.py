# https://www.acmicpc.net/problem/7568
import sys
people= []
N = int(input())

for _ in range(N):
    people.append(list(map(int,sys.stdin.readline().split())))

#BF
for outer in people:
    cnt = 1
    for inner in people:
        #문제조건
        if outer[0]<inner[0] and outer[1] < inner [1] :
            cnt+=1
    print(cnt,end=" ")
