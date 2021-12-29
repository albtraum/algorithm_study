#https://www.acmicpc.net/problem/10809
import sys
word = sys.stdin.readline().strip()
ans = ""
for i in range(26) :
    ans += str(word.find(chr(97+i)))+" "
print(ans.strip())
