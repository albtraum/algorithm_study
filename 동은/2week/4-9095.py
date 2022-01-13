# https://www.acmicpc.net/problem/9095
T = int(input())
dp = [0,1,2,4]
for i in range(1,9):
    dp.append(dp[i]+dp[i+1]+dp[i+2])
for _ in range(T):
    print(dp[int(input())])
