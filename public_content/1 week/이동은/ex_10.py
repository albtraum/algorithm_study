#https://www.acmicpc.net/problem/1946
import sys
#sys.stdin = open('test.txt')
#text input
case = int(sys.stdin.readline().strip())


for _ in range(case):
    count = int(sys.stdin.readline().strip())
    people = sorted([list(map(int, sys.stdin.readline().strip().split())) for e in range(count)], key = lambda e: e[0])

    answer = 1
    min = people[0][1]
    #1위 한 사람기준으로 정렬하고, 최소값 업데이트 하면서 진행할 것 
    for i in range(1,count):
        if min > people[i][1]:
            min = people[i][1]
            answer +=1

    print(answer)
