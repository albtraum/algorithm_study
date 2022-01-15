# https://www.acmicpc.net/problem/9012
import sys
N = int(input())
for _ in range(N):
    input = sys.stdin.readline().rstrip()
    checker = 0 
    temp = []
    for e in input:
        if e == "(":
            temp.append(e)
        elif e == ")" :
            if len(temp)!= 0:
                temp.pop()
            else :
                print("NO")
                checker = 1
                break
    if len(temp)==0 and checker == 0 :
        print("YES")
    elif len(temp)!=0 and checker == 0 :
        print("NO")
    

