# https://www.acmicpc.net/problem/10773
import sys
count = int(input())
stk=[]

for i in range(count):
    num = int(input())
    if(num == 0):
        stk.pop()
    else:
        stk.append(num)

print(sum(stk))
