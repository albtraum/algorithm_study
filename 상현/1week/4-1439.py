arr=list(input())
cnt=0
for i in range(len(arr)-1):
  if arr[i]!=arr[i+1]:
    cnt+=1
print((cnt+1)//2)

### 001 1번바뀔 때 00100 2번 바뀔 때 1개 001001 3번 바뀔 때 2개 0100101 4번 바뀔 때 2개