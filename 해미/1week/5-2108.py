# https://www.acmicpc.net/problem/2108
import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

print(round(sum(arr)/len(arr))) # 평균

arr.sort() # 중앙값
print(arr[(N-1)//2])

if N != 1: # 최빈값
    a = Counter(arr).most_common(2)
    if a[0][1] == a[1][1]:
        print(a[1][0])
    else:
        print(a[0][0])
else:
    print(arr[0])

print(arr[-1] - arr[0]) # 범위
