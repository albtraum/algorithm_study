# https://www.acmicpc.net/problem/10870
import sys
n = int(sys.stdin.readline().rstrip())
def fibo(n):
    if n>1:
        return fibo(n-1)+fibo(n-2)
    elif n == 1 :
        return 1
    elif n==0 :
        return 0 
print(fibo(n))
