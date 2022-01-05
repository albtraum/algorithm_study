import sys

k = int(sys.stdin.readline().strip())
numbers = []
for _ in range(k):
    num = int(sys.stdin.readline().strip())
    numbers.append(num) if num != 0 else numbers.pop()

print(sum(numbers))
