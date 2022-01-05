# https://www.acmicpc.net/problem/18870
import sys
N = int(input())
answer = {}
num = 0
a = list(map(int,sys.stdin.readline().split()))
a_sorted = set(a)
a_sorted = sorted(list(a_sorted))

for i in a_sorted:
    answer[i] = num
    num+=1
for j in a:
    print(answer[j],end=" ")
 
