n = int(input())
for i in range(n):
    n = bin(int(input()))[2:]
    for j in range(len(n)):
        if n[-j - 1] == '1':
            print(i, end=' ')
