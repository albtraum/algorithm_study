import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
# m이 0이 아닐 때 입력받음 (고장난 키가 있을 경우 입력 받음)
if m:
    broken = list(map(str, sys.stdin.readline().strip().split()))
else:
    broken = []

# 처음 채널 번호 100에서 이동
count = abs(100 - n)

for i in range(1000001):
    # 모든 번호에서 n으로 이동하는 경우 탐색
    for j in str(i):
        if j in broken:
            break
    # 고장난 키가 없는 번호일 경우
    else:
        # 새로 이동하는 채널 번호와 이전의 이동한 경우 비교
        count = min(count, len(str(i)) + abs(i - n))

print(count)