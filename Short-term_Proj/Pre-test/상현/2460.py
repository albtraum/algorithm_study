now=0
answer=0
for i in range(10):
  a,b = map(int,input().split())
  now-=a
  now+=b
  if now>answer:
    answer=now
print(answer)