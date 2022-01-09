#5598.py
#https://www.acmicpc.net/problem/5598
import sys

def change(alp):
    return 65+(ord(alp)-65-3)%26

words = sys.stdin.readline().strip()
ans = ""
for e in words:
    ans+= chr(change(e))
print(ans)
