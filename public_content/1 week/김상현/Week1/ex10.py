#시간초과
import sys
T=int(input())
for _ in range(T):
  arr=[]
  N=int(input())
  dp=[1 for i in range(N)]
  for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
  arr.sort(reverse=True)    # arr[?][0] 즉 배열 안의 첫 번째 원소를 기준으로 내림차순으로 정렬했다.
  for i in range(N):
    for j in range(i):      # 두 번째 원소가 이전 원소보다 큰 수열의 최대길이를 구해준다(LIS)
      if arr[i][1]>arr[j][1]:
        dp[i]=max(dp[i],dp[j]+1)
  print(max(dp))