# https://www.acmicpc.net/problem/18870
import sys
N = int(input())
ans = {}
loc_list = list(map(int,sys.stdin.readline().split()))
loc_list_sorted = set(loc_list)
loc_list_sorted = sorted(list(loc_list_sorted))
#중복 제거, 리스트 정렬을 통한 좌표 압축

cnt = 0
for e in loc_list_sorted:
    ans[e] = cnt
    cnt+=1
for e in loc_list:
    print(ans[e],end=" ")
 
