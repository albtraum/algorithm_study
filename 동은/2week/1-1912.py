# https://www.acmicpc.net/problem/1912
import sys
import math
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
# 최소값 -1001 로 해도 됨
dp = [ -math.inf for _ in range(n+1)]
# dp[n] 의미 -> 각 구간 별 최대 값
# 최대 값을 구해야 하므로, 다음 것과 더하였을 때 작아진다면, 더하지 않고, 그 부분에서 다시 시작
# 예를 들어  n번째 숫자까지의 합이 -20 n+1번째 숫자가 20 일 때 
# dp[n+1] 은 -20, 20 중, 20이 된다. 즉 dp[n+1]은 n+1번째 값으로 변경
for  i in range(1,n+1):
    dp[i] = max(dp[i-1]+nums[i-1],nums[i-1])
print(max(dp))
