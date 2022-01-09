# https://www.acmicpc.net/problem/1931
import sys
N = int(input())
time_ = []
for _ in range(N):
    time_.append(list(map(int,sys.stdin.readline().split())))
time_.sort(key = lambda x : (x[1],x[0]))
#끝나는 시간을 기준으로 함, 4 4, 3 3 과 같은 동시에 시작하면서 끝나는 것들을 
cnt =0
start = 0
end = 0
for e in time_:
    if start <= e[0] and end <= e[0]:
        cnt+=1
        # 회의 정보 넘기기 
        start,end =e[0], e[1]
print(cnt)
