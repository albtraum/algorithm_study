T = int(input())
for _ in range(T):
  words = list(input().split(" "))
  for i in words:
    print(i[::-1],end=" ")
  print()