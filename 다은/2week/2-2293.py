import sys

n, k = map(int, sys.stdin.readline().strip().split())

coin = []
dp = [0 for _ in range(k+1)]
dp[0] = 1

for _ in range(n):
    coin.append(int(sys.stdin.readline().strip()))

for i in coin:
    for j in range(1, k+1):
        if j - i >= 0:
            # 점화식
            dp[j] += dp[j-i]

print(dp[k])
