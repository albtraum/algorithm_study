# https://www.acmicpc.net/problem/10828
import sys

counts = int(input())
stk = []
for _ in range(counts):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stk.append(int(command[1]))
    elif command[0] == "pop":
        if len(stk) == 0:
            print("-1")
        else:
            print(stk.pop())
    elif command[0] == "size":
        print(len(stk))
    elif command[0] == "empty":
        if len(stk) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "top":
        if len(stk) == 0:
            print("-1")
        else: 
            print(stk[-1])
