n = int(input())
num = 0
def Fibo(a, b):
    global num

    sum = a + b

    if num == n:
        print(a)
        exit()

    num += 1
    return Fibo(b, sum)

Fibo(0, 1)

'''
def fibo(n):
    if n <= 1: return n
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))
'''