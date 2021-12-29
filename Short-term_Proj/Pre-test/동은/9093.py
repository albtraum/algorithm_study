# https://www.acmicpc.net/problem/9093
import sys
count = int(sys.stdin.readline().strip())
sen_list = [ sys.stdin.readline().split() for _ in range(count) ] 

for e in sen_list :
    for word in e:
        print(word[::-1],end=" ")
    print("")
