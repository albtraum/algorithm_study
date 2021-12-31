a = int(input())
ans = 1
if n > 0:
    for i in range(1, n+1):
        ans *= i
print(ans)