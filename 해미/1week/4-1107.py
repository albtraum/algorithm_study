# https://www.acmicpc.net/problem/1107
import sys
N = int(input())
M = int(input())

if M > 0: #0인 경우 처리
    a = list(map(int,input().split()))
else:
    a = []

broken = [0] * 10 
for x in a: #버튼이 고장나 있으면 1, 아니면 0
    broken[x] = 1

def possible(C): #C에 포함되어 있는 숫자 중에 고장난 버튼이 있는지 확인 
                 #possible을 불가능 : 0, 가능 : 버튼을 눌러야 하는 횟수 return
    if C == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while C > 0:
        if broken[C%10]:
            return 0
        l += 1
        C //= 10
    return l

ans = abs(N-100)
for i in range(0, 1000000+1): #이동할 채널 C를 정하기
    C = i
    l = possible(C)
    if l > 0:
        press = abs(C-N)
        if ans > l + press:
            ans = l + press
print(ans)
