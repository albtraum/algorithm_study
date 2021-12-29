# https://www.acmicpc.net/problem/2309
import sys
people_list = [ int(sys.stdin.readline().strip()) for _ in range(9)]
people_list.sort()
seven_list=[]
key = None
for i in range(9):
    for j in range(9):
        if (i != j) and (sum(people_list)-(people_list[i]+people_list[j])==100) :
            key = [i,j] 
for idx in range(9):
    if idx != key[0] and idx != key[1]:
        seven_list.append(people_list[idx])
for e in seven_list:
    print(e)
