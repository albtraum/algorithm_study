T=int(input())
for _ in range(T):
  N,M=map(int,input().split())
  arr=list(map(int,input().split()))
  cnt=0
  while(True):
    if max(arr)==arr[0] and M!=0:
      arr.pop(0)
      M-=1
      cnt+=1
    elif max(arr)==arr[0] and M==0:
      cnt+=1
      print(cnt)
      break
    elif max(arr)!=arr[0] and M!=0:
      arr.append(arr.pop(0))
      M-=1
    elif max(arr)!=arr[0] and M==0:
      arr.append(arr.pop(0))
      M=len(arr)-1