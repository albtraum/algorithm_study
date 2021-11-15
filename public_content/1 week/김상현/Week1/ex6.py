N=int(input())
temp=N
A=100
cycle=0
while N!=A:
    A=temp
    N=((N//10+N%10)%10)+(10*(N%10))
    cycle+=1
print(cycle)
