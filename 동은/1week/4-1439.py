# https://www.acmicpc.net/problem/1439
S = input()
cnt_0 = 0
cnt_1 = 0

#0으로 바뀌는 경우, 1로 바뀌는 경우를 나눔
for idx in range(1, len(S)):
    if S[idx-1] != S[idx]:
        if S[idx] =="0":
            cnt_0 +=1
            if cnt_1 ==0 :
                cnt_1 += 1
        elif S[idx] =="1":
            cnt_1 +=1
            if cnt_0 ==0 :
                cnt_0 += 1
# 다른 숫자를 만났을 때, 이전 숫자에 대한 카운팅이 안되어 있으므로 덧셈

print(min(cnt_0,cnt_1))
