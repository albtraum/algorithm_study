#https://www.acmicpc.net/problem/1110
import sys
answer =0

n= sys.stdin.readline().strip()
flag =1 
temp = (n)

while(flag):
    #10 미만일 경우 조건
    if int(temp)<10 and answer == 0:   
        temp="0"+temp 
    # 그 외 계산식 표현
    temp = temp[1] +str((int(temp[0])+int(temp[1])))[-1] 
    #일치할 경우 종료~
    if int(temp) == int(n) :
        flag = 0
    answer +=1
print(answer)
