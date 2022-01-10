import sys
N = int(sys.stdin.readline()) 
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True) #중량 정렬
ans = 0
for i in range(N):
    if arr[i] * (i + 1) > ans: #무게 늘리면서 로프가 견디는 무게 추가
        ans = arr[i] * (i + 1)
print(ans)