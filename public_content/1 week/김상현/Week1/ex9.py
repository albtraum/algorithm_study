def solution(N, stages):
    arr=[0]*N
    ans=[0]*N
    result=[[i for _ in range(2)] for i in range(1,N+1)]
    sol=[]
    for i in range(N):
        arr[i]=stages.count(i+1)
        ans[i]=stages.count(i+1)
    arr[i]=stages.count(i+1)
    arr[N-1]+=stages.count(N+1)
    for i in range(N-1,0,-1):
        arr[i-1]+=arr[i]
    for i in range(N):
        if arr[i]!=0:
            result[i][0]=i+1
            result[i][1]=float(ans[i]/arr[i])
        else:
            result[i][0]=i+1
            result[i][1]=0
    result.sort(key=lambda x: -x[1])
    for i in range(N):
        sol.append(result[i][0])

    return sol
        