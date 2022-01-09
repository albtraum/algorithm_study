# https://www.acmicpc.net/problem/3460
import sys
count = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(count)]
bin = []
for e in nums:
    bin.append(format(e,'b')[::-1])
for e in bin:
    for idx in range(len(e)):
        if e[idx]=='1':
            print(idx,end=" ")

# 3210
# 1101
