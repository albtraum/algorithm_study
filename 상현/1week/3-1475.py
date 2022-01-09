n=int(input())
time=sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
cnt=0
end=0
for s,e in time:
  if s>=end:
    end=e
    cnt+=1
print(cnt)
