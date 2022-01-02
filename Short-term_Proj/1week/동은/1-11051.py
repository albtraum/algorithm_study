# https://www.acmicpc.net/problem/11051
import math
N,K = map(int,input().split())
print(int( (math.factorial(N))//(math.factorial(K)*math.factorial(N-K)))%10007)
# ?? 왜이렇게 쉽게 풀리지 

