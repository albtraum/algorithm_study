T = int(input())
arr=[]
max_len=0
for _ in range(T):
  arr.append(int(input()))

arr.sort(reverse=True)
for i in range(T):
  if max_len<arr[i]*(i+1):
    max_len=arr[i]*(i+1)
print(max_len)
