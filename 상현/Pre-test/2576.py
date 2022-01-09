s=0
m=100
for i in range(7):
  num=int(input())
  if num%2==1:
    s+=num
  if num%2==1 and num<m:
    m=num
if s==0 and m==100:
  print(-1)
else:
  print(s)
  print(m)