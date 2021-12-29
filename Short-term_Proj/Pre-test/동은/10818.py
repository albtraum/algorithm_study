#https://www.acmicpc.net/problem/10818
import sys
count = int(sys.stdin.readline().strip())
nums = list(map(int,sys.stdin.readline().split()))
print(min(nums),max(nums))
