import collections

def solution(participant, completion):
    dic ={}
    temp =0
    #해시함수를 통하여 딕셔너리에 저장 
    #남은 하나의 값이 곧 완주하지 못한 선수 (전제조건, 단 한명을 제외하고 완주)
    for i in participant:
        dic[hash(i)] = i
        temp += hash(i)
    for i in completion:
        temp -= hash(i)
    
    answer = dic[temp]
        

    return answer
