N,M=map(int,input().split())
chess=[]
for i in range(N):
    chess.append(input())
modify=[]
for i in range(N-7):
  for j in range(M-7):
    first_W=0
    first_B=0
    for k in range(i,i+8):
      for l in range(j,j+8):
        if (k+l)%2==0:
          if chess[k][l]!='W':
            first_W+=1
          if chess[k][l]!='B':
            first_B+=1
        else:
          if chess[k][l]!='B':
            first_W+=1
          if chess[k][l]!='W':
            first_B+=1
    modify.append(first_W)
    modify.append(first_B)
print(min(modify))