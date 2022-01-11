import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().strip().split())
alphabet = list(sys.stdin.readline().strip().split())
alphabet.sort()

li = list(map(''.join, combinations(alphabet, l)))

for i in li:
    vowel = 0
    consonant = 0
    for j in list(i):
        if j in 'aeiou':
            vowel += 1
        else:
            consonant += 1
    if vowel >= 1 and consonant >= 2:
        print(i)
