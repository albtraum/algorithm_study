# https://www.acmicpc.net/problem/11047
import sys
N,K = map(int,input().split())
coin_list = []
for _ in range(N):
    coin = int(sys.stdin.readline().rstrip())
    # 어처피 계산 하려는 값 이상은 의미없음
    if coin <= K:
        coin_list.append(coin)
    else : 
        break
coin_list.sort(reverse=True)
cnt = 0 
sum = K

# 나눈 값의 몫이 동전 수, 그 나머지를 다음 동전으로 나눈다.
# 직접 하나씩 빼면 시간복잡도 통과 못함 (pypy3로는 가능)
while(sum != 0):
    for e in coin_list:
        temp = 0
        while(sum >= e):
            cnt +=sum//e
            sum = sum%e
print(cnt)


