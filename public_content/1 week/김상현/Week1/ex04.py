#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    new_lost=set(lost)-set(reserve)
    new_reserve=set(reserve)-set(lost)
    #여벌의 체육복을 가지고 있는 사람이 도난을 당할 수 있으므로 차집합을 이용해 겹치는 사람은 제외해준다.
    answer = n-len(new_lost)
    #1차적으로 빌려주는 것을 제외한 순수하게 본인의 체육복이 없는 사람의 수를 구했다(최솟값)
    for num in new_lost:
        if num-1 in new_reserve:
            answer+=1
            new_reserve.remove(num-1)
    #코테에서 remove 시간이 오래걸려서 되도록이면 안쓰는게 좋다고 배웠는데 마땅한 대체방법을 모르겠어서 사용했습니다
    #먼저 체육복을 도난당한 학생의 번호-1의 번호를 가지고 있는 학생이 여벌이 있는지 확인하고 있으면 answer에 1더하고
    #빌려준 학생을 여벌이 있는 학생에서 지운다
        elif num+1 in new_reserve:
            answer+=1
            new_reserve.remove(num+1)
    #마찬가지로 도난당한 학생의 번호+1도 확인해준다.
    return answer