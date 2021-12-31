T = int(input())
for _ in range(T):
  k = int(input())
  n = int(input())
  for _ in range(n):
    f0 = [i for i in range(1,n+1)]
  for i in range(k*n):
    if i%n==0:
      f0.append(1)
    else:
      f0.append(f0[n+i-1]+f0[i])
  print(f0[n*(k+1)-1])

