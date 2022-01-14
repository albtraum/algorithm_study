import sys
input = sys.stdin.readline

n = int(input())

wine = []

for _ in range(n):
    wine.append(int(input()))

dp = [0]*n
dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]
if n > 2:
    dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])

for i in range(3, n):
    # dp[i-1] -> i번째를 마시지 않을 경우
    # dp[i-3] + wine[i-1] + wine[i] -> i번째와 i-1번째를 마실 경우
    # dp[i-2] + wine[i] -> i번째를 마시고 i-1번째를 마시지 않을 경우
    dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

print(dp[-1])
