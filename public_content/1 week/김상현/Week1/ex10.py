#시간초과
T=int(input())
for _ in range(T):
  arr=[]
  N=int(input())
  dp=[1 for i in range(N)]
  for _ in range(N):
    arr.append(list(map(int,input().split())))
  arr.sort(reverse=True)
  for i in range(N):
    for j in range(i):
      if arr[i][1]>arr[j][1]:
        dp[i]=max(dp[i],dp[j]+1)
  print(max(dp))