#https://www.acmicpc.net/problem/11047
import sys
N, K = map(int, input().split())
arr = []
num = 0
for i in range(N):
    arr.append(int(input()))
arr.sort(reverse=True) #역순으로 정렬한 후 큰 돈부터 나눠줌
for i in range(N): 
    if arr[i] <= K: 
        num += K//arr[i] #나누기의 몫 구함
        K = K%arr[i] #나누기의 나머지 구함
print(num)

