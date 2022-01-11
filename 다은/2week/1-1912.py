import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split()))

# 자신의 앞에 있는 수와 더했을 때 자기 자신보다 더 크면 값을 변경 -> 연속되는 수를 더하면서 얻을 수 있는 최대 값 저장
for i in range(1, n):
    temp = numbers[i-1] + numbers[i]
    if temp > numbers[i]:
        numbers[i] = temp

print(max(numbers))
