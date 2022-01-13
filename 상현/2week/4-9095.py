T=int(input())
N=[1,2,4]
for j in range(3,11):
  N.append(N[j-3]+N[j-2]+N[j-1])
for i in range(T):
  A=int(input())
  print(N[A-1])
