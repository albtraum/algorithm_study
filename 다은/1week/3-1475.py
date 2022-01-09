import sys

number = sys.stdin.readline().strip()
numbers = [int(i) for i in number]

count = 0
for i in range(9):
    if i == 6:
        num = (numbers.count(i) + numbers.count(9))/2
        if num%1 >= 0.5:
            num = int(num)+1
        else:
            num = int(num)
        if num > count:
            count = num
    elif numbers.count(i) > count:
        count = numbers.count(i)
print(count)