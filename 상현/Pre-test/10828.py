import sys
T=int(input())
arr=[]
for i in range(T):
  commend=sys.stdin.readline().split()
  if commend[0]=="push":
    arr.append(commend[1])
  elif commend[0]=="pop":
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
  elif commend[0]=="top":
    if len(arr)==0:
      print(-1)
    else:
      print(arr[len(arr)-1])