import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

numbers = [i for i in range(1, n+1)]

# numbers에서 m개를 뽑은 모든 조합
for i in sorted(list(permutations(numbers, m))):
    for idx in range(len(i)):
        print(i[idx], end=" ")
    print()
