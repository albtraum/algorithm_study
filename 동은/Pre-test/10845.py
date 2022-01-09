# https://www.acmicpc.net/problem/10845
import sys

## file 
#input = open('211231_test\input.txt')
#counts = int(input.readline())

counts = int(input())
que = []
front = 0 
rear = 0 
for _ in range(counts):
    command = sys.stdin.readline().split()
    #command = input.readline().split()
    if command[0] == "push":
        que.insert(0,int(command[1]))
        front +=1
    elif command[0] == "pop":
        if len(que) == 0:
            print("-1")
        else:
            print(que.pop())
            rear+=1
    elif command[0] == "size":
        print(len(que))
    elif command[0] == "empty":
        if len(que) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(que) == 0:
            print("-1")
        else: 
            print(que[-1])
    elif command[0] == "back":
        if len(que) == 0:
            print("-1")
        else: 
            print(que[0])
