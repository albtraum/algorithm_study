k = int(input())
arr = [0]
for i in range(k):
    n = int(input())
    if n == 0: 
        arr.pop() 
    else: 
        arr.append(n) 
print(sum(arr))

