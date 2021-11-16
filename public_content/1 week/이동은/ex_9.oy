def solution(N, stages):
    dict={}
    for stage in range(1,N+1):
        num=0
        for e in stages:
            if e>=stage :
                num+=1
        if num == 0:
            dict[stage] = 0.0
        else : 
            dict[stage] = stages.count(stage)/num
    
        temp = sorted(dict.items(), key=lambda x:x[1],reverse=True)
        answer =[]
        for e in temp:
            answer.append(e[0])
    return answer
