#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    from collections import Counter   
    #동명이인이 있기 때문에 not in 을 사용하는 것보다 Counter를 사용하는게 좋을 것 같다.
    p=Counter(participant)            
    #참가자를 Counter를 이용해주면 {sanghyeon:1,Tom:2} 와 같이 딕셔너리형태로 나온다.
    c=Counter(completion)             
    #마찬가지로 완주한 사람도 해주면 각 이름별로 완주자가 몇 명인지 나온다.
    for person in participant:
        if p[person]!=c[person]:      
    #참가자 이름별로 p에서는 몇 명인지 c에서는 몇 명인지 비교하여 다를 경우가 생기면
            return person            
    #그 이름이 완주하지 못한 사람의 이름이다.