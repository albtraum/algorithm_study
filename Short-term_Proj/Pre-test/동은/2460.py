# https://www.acmicpc.net/problem/2460
import sys
people_list = [ list (map(int,sys.stdin.readline().split())) for _ in range(10)]
ans =0 
count =0 
for e in people_list:
    count += (e[1] - e[0])
    if count > ans:
        ans = count
print(ans) 

