import sys
N,K = map(int,sys.stdin.readline().split(' '))
arr=[]
count=0
for _ in range(N):
  arr.append(int(sys.stdin.readline()))
i=N-1
while (K>0):
  if K>=arr[i]:
    K-=arr[i]
    count+=1
  else:
    i-=1

print(count)