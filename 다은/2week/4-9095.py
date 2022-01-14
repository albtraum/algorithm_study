import sys
input = sys.stdin.readline

t = int(input())

case = []
for _ in range(t):
    case.append(int(input()))

dp = [0, 1, 2, 4]

if max(case) > 3:
    for i in range(4, max(case) + 1):
        # 점화식 dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in case:
    print(dp[i])