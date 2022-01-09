N,K=map(int,input().split())
cnt=0
for i in range(1,N+1):
  if N%i==0:
    cnt+=1
    num=i
    if cnt==K:
      break
    else:
      num=0
print(num)