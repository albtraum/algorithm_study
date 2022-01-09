# https://www.acmicpc.net/problem/1439
import sys
N = input()
arr = []
arr.append(N[-1]) #배열 마지막 값 처리
for i in range(len(N)-1): #중복되는 값 제거
    if N[i] != N[i+1]:
        arr.append(N[i])
print(min(arr.count('1'), arr.count('0'))) #배열에 작게 저장된 값을 찾아 뒤집기