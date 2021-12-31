arr = []
for i in range(9):
    arr.append(int(input()))
 
max = max(arr)
num = arr.index(max)
print(max)
print(num+1)