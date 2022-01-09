# https://www.acmicpc.net/problem/1158
import sys
n,k = map(int,sys.stdin.readline().split())
print("<",end="")
nums = [ x for x in range(1,n+1)]
remove_idx = k-1  #삭제 될 부분
before_idx = 0 #이전 인덱스
check = []
for i in range(n):
    if i==n-1:
        print(nums.pop(remove_idx),end="")
    else:
        print(nums.pop(remove_idx),end=", ")
    if len(nums) ==0:
        continue
    before_idx = remove_idx    
    remove_idx = ( before_idx + (k-1) ) % len(nums)

print(">",end="")

# 1 2 3 4 5 6 7 

# 0 1 2 3 4 5 6 

# 3 6 2 7 5 1 4 
# 2 5 1 6 4 0 3
