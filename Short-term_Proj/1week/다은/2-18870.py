import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().strip().split()))
value = {}
list2 = sorted(set(list))

for i in range(len(list2)):
    value[list2[i]] = i

for i in list:
    print(value[i], end=' ')
