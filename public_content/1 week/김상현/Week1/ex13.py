def solution(progresses, speeds):
  cnt=0
  arr=[0]
  # sum함수 사용을 위해 0을 넣어준다
  while min(progresses)<100:
    for i in range(len(progresses)):
      progresses[i]+=speeds[i]
    # 모든 경우 작업을 진행한다
    for j in range(sum(arr),len(progresses)):
      if progresses[j]>=100 and (j==0 or progresses[sum(arr)+cnt]>=100):
        cnt+=1
    # 작업이 한 사이클 돌면 두 가지를 확인해준다. 기능이 100%완료되었는지와 그 기능 앞의 작업이 모두 끝났는지
    if cnt!=0:
      arr.append(cnt)
      cnt=0
    # 위에서 뽑은 개수를 넣어준다 
  arr.remove(0)
  # sum을 위해 넣은 0을 제거해준다
  return arr
