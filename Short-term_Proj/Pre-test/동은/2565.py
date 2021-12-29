#https://www.acmicpc.net/problem/2562
import sys

input = [ int(sys.stdin.readline().strip()) for _ in range(9) ]   
print( "%d\n%d" %(max(input),input.index(max(input)) + 1))
