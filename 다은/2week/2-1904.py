import sys

n = int(sys.stdin.readline().strip())
dp = [0 for _ in range(n+2)]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    # 출력 초과로 반복문 실행할 때 마다 15746으로 나눈 나머지 값을 저장해야함
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])
