import sys

n = int(sys.stdin.readline().strip())
time = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    time.append([start, end])

time.sort(key = lambda x:(x[1], x[0]))

end_time = 0
count = 0
for i, j in time:
    if i >= end_time:
        count += 1
        end_time = j
print(count)