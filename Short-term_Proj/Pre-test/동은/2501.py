# https://www.acmicpc.net/problem/2501
import sys
m,n = map(int,sys.stdin.readline().split())
n_list = []
for i in range(1,m+1):
    if m%i == 0 :
        n_list.append(i)
if n>len(n_list):
    print("0")
else :
    print(n_list[n-1])
