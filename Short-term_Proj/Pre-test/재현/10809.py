s = list(map(str, input()))
a = list('abcdefghijklmnopqrstuvwxyz')
ans = []
for i in range(len(a)):
    ans.append(-1)
# ans = [-1 for i in range(len(alpha))] 5번부터 7번째 줄 줄인거
for i in range(len(s)):
    if ans[a.index(s[i])] == -1:
        ans[a.index(s[i])] = i      
for j in ans:
    print(j, end = " ")