T=int(input())
for i in range(T):
  n=int(input())
  cnt=0
  while(True):
    if n%2==1:
      print(cnt,end=" ")
    n//=2
    cnt+=1
    if n==0:
      break