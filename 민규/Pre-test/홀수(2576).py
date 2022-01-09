import sys

input = sys.stdin.readline
li = [int(input()) for i in range(7)]

li2 = []

for i in li:
    if i % 2 == 1:
        li2.append(i)

if not li2:
    print("-1")
    exit()

print(sum(li2))
print(min(li2))
