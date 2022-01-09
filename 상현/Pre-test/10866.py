import sys
from collections import deque
T=int(input())
arr=deque()
for i in range(T):
  commend=sys.stdin.readline().split()
  if commend[0]=="push_front":
    arr.appendleft(commend[1])
  elif commend[0]=="push_back":
    arr.append(commend[1])
  elif commend[0]=="pop_front":
    if len(arr)==0:
      print(-1)
    else:
      print(arr.popleft())
  elif commend[0]=="pop_back":
    if len(arr)==0:
      print(-1)
    else:
      print(arr.pop())
  elif commend[0]=="size":
    print(len(arr))
  elif commend[0]=="empty":
    if len(arr)==0:
      print(1)
    else:
      print(0)
  elif commend[0]=="front":
    if len(arr)==0:
      print(-1)
    else:
      print(arr[0])
  elif commend[0]=="back":
    if len(arr)==0:
      print(-1)
    else:
      print(arr[-1])
