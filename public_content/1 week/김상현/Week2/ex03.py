def solution(n, arr1, arr2):
  one=[[0 for _ in range(n)] for _ in range(n)]
  two=[[0 for _ in range(n)] for _ in range(n)]
  secret=[[0 for _ in range(n)] for _ in range(n)]
  real=[]
  for i in range(n):
    cnt=0
    num=arr1[i]
    while cnt<n:
      if num%2==1:
        one[i][cnt]=1
      else:
        one[i][cnt]=0
      cnt+=1
      num//=2
    one[i].reverse()
  for i in range(n):
    cnt=0
    num=arr2[i]
    while cnt<n:
      if num%2==1:
        two[i][cnt]=1
      else:
        two[i][cnt]=0
      cnt+=1
      num//=2
    two[i].reverse()
  for i in range(n):
    for j in range(n):
      if one[i][j]==0 and two[i][j]==0:
        secret[i][j]=" "
      else:
        secret[i][j]="#"
  for i in range(n):
    real.append("".join(secret[i]))  
  return real