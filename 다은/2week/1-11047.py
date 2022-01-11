import sys

n, k = map(int, sys.stdin.readline().strip().split())
money = []
count = 0

for i in range(n):
  money.append(int(input()))

# 동전 개수의 최댓값이므로 제일 큰 동전부터 시작
idx = len(money) - 1

# 입력받은 k가 0이 되기 전까지
while k > 0:
  if (k // money[idx]) >= 1:
    # 몫만큼 개수를 증가
    count += (k // money[idx])
    # 남은 돈
    k %= money[idx] 
  # 작은 단위로
  idx -= 1

print(count)
