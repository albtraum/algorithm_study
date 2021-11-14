#https://www.acmicpc.net/problem/1100
height=1
#높이 8까지만 while문을 작동시키기 위한 장치
sum=0
point_w=0
#홀수행인지 짝수행인지를 판별하기 위한 장치
#체스판의 높이
while height<9:
  arr=list(input())
  if height%2==0:
    point_w=1
  else:
    point_w=0
  #하얀색이 첫번째인지 두번째인지를 정해준다.
  for i in range(8):
    if arr[i]=="F" and point_w==0 and i%2==0:
      sum+=1
    elif arr[i]=="F" and point_w==1 and i%2==1:
      sum+=1
    else:
      pass
  #F가 나왔을 때 홀수행이면 홀수열에 F가 있는지(인덱스가 0부터 시작이므로 홀수를 0 짝수를 1로 표현)
  #짝수행이면 짝수열에 F가 있는지 확인하고 맞으면 sum에 1을 더해준다.
  height+=1
print(sum)