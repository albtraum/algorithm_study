#BFS논리 사용(틀림 왜 틀린지 모르겠음..)
def solution(n, computers):
  from collections import deque
  visited=[1]*n    #방문을 하면 0으로 바꿔서 sum이 0이 될 때까지(모두 방문할 때까지)진행
  visited[0]=0    #첫 네트워크의 노드1
  queue=deque([0])
  net=1
  while True:
    v=queue.popleft()   #1에 연결된 부분 조사
    reset=0     #조건을 만족하지 않을 경우를 위해 만들었는데 sum까지 0이라면 끝이고 그게 아니라면 상황에 따라
                #새로운 네트워크를 생성하고자 만든 변수다.
    for i in range(n):
      if computers[v][i]==1 and v!=i and visited[i]==1:     #조건1 연결 조건2 본인X 조건3 방문X
        queue.append(i)       #만족하면 큐에 추가
        visited[i]=0          #방문
        reset+=1
      else:
        if i==n-1 and reset==0:     #끝까지 확인했는데 reset이 0인 경우
          if sum(visited)==0:       #경우1: 모든 방문이 끝났을 때
            return net
          else:
            if visited[v]==1 or (visited[v]==0 and len(queue)==0):    #경우2: 고립된 경우
              net+=1                                                 #경우3: 연결은 되어있지만 앞에서 방문했고 큐에 남은게 없는 경우
              queue.append(visited.index(1))
              visited[visited.index(1)]=0
            else:                                                   #경우4: 연결은 되어있지만 앞에서 방문한 경우(큐에 남아있음)
              queue.append(visited.index(1))
              visited[visited.index(1)]=0