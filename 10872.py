num = int(input())
ans = 1

if num > 0:
    for i in range(1, num+1):
        ans *= i
print(ans)