# 시간초과

N=int(input())
arr=[]
for i in range(N):
  num=int(input())
  if num==0 and len(arr)==0:
    print(0)
  elif num==0 and len(arr)>0:
    print(arr.pop(arr.index(max(arr))))
  else:
    arr.append(num)