# https://www.acmicpc.net/problem/1475
from collections import Counter
import math
N = input()
# 9를 6으로 통일
N = N.replace("9","6")
ans = 0
for i in range(9):
    if  str(i)== "6":
        # 6인 경우 2로 나누고, 올림처리 
        ans = max(ans, math.ceil(Counter(N)[str(i)]/2))
    else:
        ans = max(ans,Counter(N)[str(i)])
print(ans)
