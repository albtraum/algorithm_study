# https://www.acmicpc.net/problem/2775
import sys
T = int(input())
ans_list =[]
for _ in range(T):
    people = []
    m = int(input())
    n = int(input())
    for floor in range(m):
        for width in range(1,n+1):
            if floor == 0 :
                people.append(width)
            elif width > 1 : 
                people[width-1] += people[width-2]
    ans_list.append(sum(people))
for e in ans_list:
    print(e)

# 2 => 1 4 10
# 1 => 1 3 6 
# 0 => 1 2 3
#


# 2 => 1 4 10 20
# 1 => 1 3 6 10
# 0 => 1 2 3 4

