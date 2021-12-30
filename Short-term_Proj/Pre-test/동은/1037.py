# https://www.acmicpc.net/problem/1037
import sys 
counts = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().split()))
numbers.sort()
if len(numbers)%2 == 0:
    print(numbers[int(len(numbers)/2)]*numbers[int(len(numbers)/2)-1])
else :
    print(numbers[int(len(numbers)/2)]**2)
