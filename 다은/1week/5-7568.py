import sys

n = int(sys.stdin.readline().strip())

people = []
for _ in range(n):
  weight, height = map(int, sys.stdin.readline().strip().split())
  people.append([weight, height])

for i in range(n):
  rank = 1
  for j in range(n):
    # 자신과의 비교가 아니고
    if i != j:
      # 자신보다 덩치가 클 때 순위 + 1
      if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
        rank += 1
  print(rank, end=' ')
