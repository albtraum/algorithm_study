n = int(input())
a = list(map(int, input().split())) # a에 list로 숫자들을 받아준 뒤, sum이라는 새로운 리스트를 만들어 준다.
sum = [a[0]] # sum의 0번째 인덱스에는 비교를 위해 a[0]을 넣어준다.
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1])) #sum의 i번째 인덱스와 a의 i + 1번째 인덱스의 숫자를 합한 값과 a의 i + 1번째 숫자를 비교하여 더 큰 숫자를 sum리스트에 넣어준다.
print(max(sum)) #sum리스트 중에 가장 큰 수를 출력한다.