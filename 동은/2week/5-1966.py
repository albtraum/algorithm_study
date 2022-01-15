# https://www.acmicpc.net/problem/1966
import sys
from collections import deque
T = int(input())
for _ in range(T):
    papers_cnt, loc = map(int,sys.stdin.readline().split())
    deq=deque()
    temp_prior = list(map(int,sys.stdin.readline().split()))
    #큐에 입력 단계
    for i in range(papers_cnt):
        deq.append([i+1,temp_prior[i]])
    while(len(deq)!=0):
        
print(deq)
deq.rotate(3)
print(deq)
