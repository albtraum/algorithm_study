#https://www.acmicpc.net/problem/1546
import sys
count = int(sys.stdin.readline().strip())
subjects = list(map(int,sys.stdin.readline().strip().split()))
max_score = max(subjects)
renew = []
for e in subjects:
    renew.append(e/max_score*100)
print(sum(renew)/count)
