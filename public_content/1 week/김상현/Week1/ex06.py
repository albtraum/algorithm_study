N=int(input())
temp=N
# N을 바꿔줄 것이기 때문에 잠시 temp에 저장해둔다로 값을 지정해준다
A=100
# 100보다 작은 수이므로 한 사이클은 돌도록 100으로 지정한다.
cycle=0
while N!=A:
    A=temp
    N=((N//10+N%10)%10)+(10*(N%10))
    cycle+=1
print(cycle)
