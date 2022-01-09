#https://www.acmicpc.net/problem/2576
import sys
input = [ int(sys.stdin.readline().strip()) for _ in range(7)]
odd_list=[]
for e in input:
    if e%2 == 1:
        odd_list.append(e)

if len(odd_list)== 0:
    print(-1)
else :
    print("%d\n%d" %(sum(odd_list),min(odd_list)))
