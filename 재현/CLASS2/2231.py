#2231
def sSum(a):
    return a + sum(map(int, list(str(a))))

n = int(input())
L = len(str(n))
init = ( n - L*9 ) if n-L*9 > 0 else 1
answer = [i for i in range(init, n) if sSum(i) == n]
if len(answer) == 0:
    print(0)
else:
    print(answer[0])
'''
if n = 1234?
    자리수 X 9
    4 x 9 = 36
    1234 - 36 = 1198
    123456
    6*9 = 54
    123456 - 54 = 123402
    123402 + 1 + 2 + 3 + 4+ 2
    123414
    123403 + 1 + 2+ 3+ 4+ 3
    123416

    1199 > 1199 + 1 + 1 + 9 + 9
    1219
    1209 > 1209 + 1 + 2 + 0 + 9
    1221

if 생성자 = 1234
    1234 + 1 + 2 + 3 + 4

IF 생성자 = 9999
    9999 + 9 + 9 + 9 + 9
'''