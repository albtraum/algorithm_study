def solution(n, lost, reserve):
    
    count = 0
    
    
    new_lost =[]
    temp = reserve.copy()
    for e in reserve:
        if e in lost:
            temp.remove(e)
            lost.remove(e)

    ori = len(lost)

    for e in reserve : 
        if e in temp : 
            if (e-1 in lost):
                temp.remove(e)
                lost.remove(e-1)
                count +=1
            elif (e+1 in lost):
                temp.remove(e)
                lost.remove(e+1)
                count +=1 
    return n-ori+count
