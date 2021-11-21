#https://www.acmicpc.net/problem/1157
import sys
import collections
word = sys.stdin.readline().strip().upper()
#모두 대문자로 바꿔줌
counter =  collections.Counter(word).most_common()
#각 문자별 나온 횟수 세줌, 그리고 most_commnon은 가장 많이 나온 순서대로 정렬
if len(word) > 1 and (counter[0][1] == counter[1][1]):
    print("?")
    exit()
print(counter[0][0])

