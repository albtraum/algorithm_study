import sys

n = int(sys.stdin.readline().strip())
triangle = []
for _ in range(n):
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    triangle.append(numbers)
dp = triangle.copy()

for i in range(1, n):
    for j in range(len(triangle[i])):
        num = []
        if j-1 >= 0:
            num.append(triangle[i-1][j-1] + triangle[i][j])
        if j+1 <= len(triangle[i-1]):
            num.append(triangle[i-1][j] + triangle[i][j])
        dp[i][j]=max(num)
print(max(dp[n-1]))

