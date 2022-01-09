n = int(input())
m = list(map(int, input().split()))
max = m[0]
min = m[0]

for i in range(n):
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)​