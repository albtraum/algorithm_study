###틀림 다시다시
def solution(N, stages):
    arr=[[i for _ in range(2)] for i in range(1,N+1)]
    for i in range(len(arr)):
        arr[i][1]=0
    ans=[]
    for i in stages:
        for j in range(len(arr)):
            if i>=arr[j][0]:
                arr[j][1]+=1
    for i in range(1,N+1):
        arr[i-1][1]=float(stages.count(i)/arr[i-1][1])
    arr.sort(key=lambda x : -x[1])    
    for i in range(N):
        ans.append(arr[i][0])
    return ans