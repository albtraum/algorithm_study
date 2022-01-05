T = int(input())
index=[]
arr = [0 for i in range(T)]
arr = list(map(int,input().split(' ')))
sub_arr = sorted(list(set(arr)))

dic = {sub_arr[i] : i for i in range(len(sub_arr))}

for i in arr:
  print(dic[i],end = ' ')