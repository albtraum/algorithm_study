from collections import Counter
import sys
T = int(sys.stdin.readline())
stat = []
for i in range(T):
  stat.append(int(sys.stdin.readline()))

print(int(round(sum(stat)/len(stat),0)))
print(sorted(stat)[T//2])
from collections import Counter
k=Counter(stat).most_common()
cnt=0
k.sort(key=lambda x: (-x[1],x[0]))
for i in range(len(k)):
  if k[0][1]==k[i][1]:
    cnt+=1
if cnt>1:
  print(k[1][0])
else:
  print(k[0][0])
print(max(stat)-min(stat))
