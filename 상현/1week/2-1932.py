T=int(input())
arr=[0]*501
for i in range(T):
  arr[i]=list(map(int,input().split(' ')))
for i in range(1,T):
  for j in range(len(arr[i])):
    if j==0:
      arr[i][j]+=arr[i-1][0]
    elif j==len(arr[i])-1:
      arr[i][j]+=arr[i-1][len(arr[i-1])-1]
    else:
      arr[i][j]+=max(arr[i-1][j-1],arr[i-1][j])

max=0
for i in range(T):
  if max<arr[T-1][i]:
    max=arr[T-1][i]
print(max)