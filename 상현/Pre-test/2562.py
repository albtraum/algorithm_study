B=0
num=0
for i in range(9):
  A=int(input())
  if A>B:
    B=A
    num=i+1
print(B)
print(num)
