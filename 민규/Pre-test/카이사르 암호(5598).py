import sys

input = sys.stdin.readline
word = input().strip()
answer = []

for i in word:
    if 'D' <= i <= 'Z':
        answer.append(chr(ord(i)-3))
    else:
        answer.append(chr(ord(i)+23))
print("".join(answer))
