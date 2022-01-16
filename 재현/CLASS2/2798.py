#2798
from itertools import combinations
import sys
n, m = map(int, sys.stdin.readline().strip().split())
nlist = list(map(int, input().split()))
ans = 0
# ans = sorted([sum(combi) for combi in combinations(nlist, 3) if sum(combi) <= m])
# print(ans[-1])


# for idx, combi in enumerate(combinations(nlist, 3)):
for i in (combinations(nlist, 3)):
    # nlist = sum(combi)
    nlist = sum(i)
    if nlist == m:
        print(nlist)
        sys.exit(0)
    if nlist > m:
        continue
    else:
        ans = max(ans, nlist)
print(ans)