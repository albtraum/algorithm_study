# https://www.acmicpc.net/problem/2108
import sys
from collections import Counter
N = int(input())
temp =[] 
for _ in range(N):
    temp.append(int(sys.stdin.readline().rstrip()))
temp.sort()
print(round(sum(temp)/N))
print(temp[(len(temp)-1)//2])


if N==1:
    print(temp[0]) 
#최빈값 여러개 일 때 
elif Counter(temp).most_common()[0][1] == Counter(temp).most_common()[1][1]:
    print(Counter(temp).most_common()[1][0])
    #2번째로 빈도 수 적은거 출력
else :
    print(Counter(temp).most_common()[0][0])
print(abs(max(temp)-min(temp)))
