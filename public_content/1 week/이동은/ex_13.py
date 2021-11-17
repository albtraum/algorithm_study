#https://programmers.co.kr/learn/courses/30/lessons/42586
import math
def solution(progresses, speeds):
    
    day = []
    answer = [] 
    for i in range(len(progresses)):

        day.append(math.ceil((100-progresses[i])/speeds[i]))

    j=0
    point =0
    i=0
    for _ in range(max(day)):
        i += point
        point = 0

        for idx in range(i,len(day)):
            if(day[i]>=day[idx]):
                point += 1
            else:break
        answer.append(point)
        if(day[i]==max(day)):
            break

    return answer
