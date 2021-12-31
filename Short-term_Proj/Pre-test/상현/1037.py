num= int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
print(arr[0]*arr[num-1])