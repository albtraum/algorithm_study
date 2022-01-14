from itertools import permutations
a, b = map(int,input().split())
arr=[]
for i in range(a):
  arr.append(str(i+1))
result=list(permutations(arr,b))

for i in range(len(result)):
  print(' '.join(result[i]))