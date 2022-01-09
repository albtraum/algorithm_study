T=int(input())
arr=[0 for _ in range(301)]
pnt=[0 for _ in range(301)]
for i in range(T):
  arr[i]=int(input())
pnt[0]=arr[0]
pnt[1]=arr[0]+arr[1]
pnt[2]=max(arr[0]+arr[2],arr[1]+arr[2])
for i in range(3,T):
  pnt[i]=max(pnt[i-3]+arr[i-1]+arr[i],pnt[i-2]+arr[i])
print(pnt[T-1])