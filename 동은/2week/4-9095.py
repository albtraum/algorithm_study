# https://www.acmicpc.net/problem/9095
T = int(input())
dp = [0,1,2,4]
# 1,2,3을 표현하는 경우의수. 각 표현가능한 수는 a[n] = a[n-1]+a[n-2]+a[n-3]의 식으로 표현 가능하다.
for i in range(1,9):
    dp.append(dp[i]+dp[i+1]+dp[i+2])
for _ in range(T):
    print(dp[int(input())])
