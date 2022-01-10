# https://www.acmicpc.net/problem/1904
N = int(input())
dp = [ 0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
# 규칙은 쓰다보면 쉽게 파악 가능
for i in range(3,N+1):
    dp[i] = (dp[i-1]+dp[i-2])%15746
print(dp[N])
