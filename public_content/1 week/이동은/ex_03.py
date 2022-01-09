import math
import operator
def solution(answers):
    #패턴 저장 
    per_1= [1,2,3,4,5]* math.ceil (len(answers)/5)
    per_2= [2,1,2,3,2,4,2,5]*math.ceil(len(answers)/8)
    per_3= [3,3,1,1,2,2,4,4,5,5]*math.ceil(len(answers)/4)

    player=[0]*3
    #점수 계산
    for idx in range(len(answers)):
        if per_1[idx] == answers[idx]:
            player[0]+=1
        if per_2[idx] == answers[idx]:
            player[1]+=1
        if per_3[idx] == answers[idx]:
            player[2]+=1
    answer = []

    temp={}
    for key in range(1,4):
        if(len(player) < key):
            break
        temp[key] = player[key-1]
    #특정 문자를 제거하는 함수 
    #filter((k).__ne__) 특정문자 k 를 제거 함
    player=list(filter((0).__ne__, player))
    flag=1
    #정렬 기준을 정하여 역순으로 배치 
    tem = sorted(temp.items(), key=lambda x : x[1],reverse=True)

    if len(tem) == 1:
        max_num = tem[0][1]
    elif len(tem) == 2:
        max_num = max(tem[0][1],tem[1][1])
    elif len(tem) == 0 :
        flag=0
    else :
        max_num = max(tem[0][1],tem[1][1],tem[2][1])

    idx_save = []
    for i in range(len(tem)):
        if(tem[i][1] == max_num):
            idx_save.append(i)
    idx_save.sort()
    i=0
    for i in range(len(idx_save)):    
        answer.append(tem[i][0])
    if flag==0:
        answer = []
    return answer
