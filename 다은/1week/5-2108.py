import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))
 
# 산술게임
print(round(sum(numbers)/len(numbers)))

# 중앙값
temp = sorted(numbers)
print(temp[len(numbers)//2])

# 최빈값
temp = Counter(temp).most_common()
if len(temp) > 1 and  temp[0][1]==temp[1][1]:
    print(temp[1][0])
else:
    print(temp[0][0])

# 범위
temp = sorted(numbers)
print(temp[-1]-temp[0])
