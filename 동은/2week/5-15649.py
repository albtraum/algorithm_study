# https://www.acmicpc.net/problem/15649
from itertools import permutations

N, M = map(int,input().split())
temp =[]
for i in range(1,N+1):
    temp.append(i)
temp =list(permutations(temp,M))
for e in temp:
    for op in e:
        print(op,end=" ")
    print("")
