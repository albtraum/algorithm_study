import sys

s = sys.stdin.readline().strip()

temp = 0
num = []

for i in s:
    # 앞선 숫자와 다를 경우 num 리스트에 추가
    if temp != i:
        num.append(i)
        temp = i

# num 리스트에서 0과 1의 개수 중 작은 수 출력
print(min(num.count('0'), num.count('1')))