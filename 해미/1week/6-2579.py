import sys
N = int(sys.stdin.readline())
stairs = []
dp = []
for i in range(N):
    stairs.append(int(sys.stdin.readline()))

if N==1: #계단이 1개일 떄
    print(stairs[0])
    exit()
elif N == 2: #계단이 2개일 떄
    print(max(stairs[0]+stairs[1], stairs[1]))
    exit()
#계단이 3개 이상일 떄
dp.append(stairs[0])
dp.append(max(dp[0]+stairs[1], stairs[1]))
dp.append(max(dp[0]+stairs[2], stairs[1]+stairs[2]))

for i in range(3, N): #중간에 더해야 할 계단 숫자합 재귀로 계산함
    dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))

print(dp[-1])
 