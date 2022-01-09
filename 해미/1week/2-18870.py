# https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr_sorted = list(sorted(set(arr)))
dic = {value: index for index, value in enumerate(arr_sorted)} #dic 이용한 자료 정렬 {Key1:Value1, Key2:Value2, Key3:Value3, ...}

for element in arr:
    print(dic[element], end= " ")