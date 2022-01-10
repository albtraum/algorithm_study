#https://www.acmicpc.net/problem/1912
#이거 싸피 시험에서 나왔던 문제!!!
import sys 
N = int(sys.stdin.readline()) 
num = list(map(int, sys.stdin.readline().split())) 
arr = [0]*N 
arr[0] = num[0] 
for i in range(1,N): 
    arr[i] = max(arr[i-1]+num[i], num[i]) #지금 위치의 값을 전의 값에 현재값을 연산한 것으로 바꿀지, 아니면 현재 값으로 유지할지 계산
print(max(arr))