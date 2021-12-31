import sys

n = int(sys.stdin.readline())
answer = 1
for i in range(1, n+1):
    if n != 0:
        answer = answer * i
    else:
        break

print(answer)
