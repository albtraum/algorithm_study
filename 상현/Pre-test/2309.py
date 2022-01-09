arr=[]
for i in range(9):
  arr.append(int(input()))
two=sum(arr)-100
for i in range(9):
  for j in range(i+1,9):
    if arr[i]+arr[j]==two:
      first=i
      second=j
arr.remove(arr[first])
arr.remove(arr[second-1])
arr.sort()
for i in range(7):
  print(arr[i])