import sys
num = int(input())
a = list(map(int, sys.stdin.readline().strip().split()))
max_num = (max(a))
ans = []
for i in a:
    ans.append(i/max_num*100)
ans = sum(ans)/num
print(ans)