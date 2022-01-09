import sys
T=int(input())
for _ in range(T):
  arr=[]
  N=int(input())
  for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
  arr.sort()    # 배열 안의 첫 번째 원소를 기준으로 오름차순으로 정렬했다.
#이 때 서류 1등을 했다는 것은 면접 결과에 상관없이 무조건 뽑히므로 서류1등을 뽑아놓고 면접을 내림차순으로 가장 긴 수열로 뽑으면된다
  max=arr[0][1]
  cnt=1
  for i in range(1,N):
    if max>arr[i][1]:
      max=arr[i][1]
      cnt+=1
  print(cnt) 