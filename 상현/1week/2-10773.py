T=int(input())
arr=[]
for i in range(T):
  num=int(input())
  if num!=0:
    arr.append(num)
  else:
    arr.pop()
print(sum(arr))