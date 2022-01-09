#https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    winner = []
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    #각 수포자들의 찍는 패턴을 배열로 만들어줬다.
    one_sol=0
    two_sol=0
    three_sol=0
    for i in range(len(answers)):
        if answers[i]==one[i%5]:
            one_sol+=1
        if answers[i]==two[i%8]:
            two_sol+=1
        if answers[i]==three[i%10]:
            three_sol+=1
    #어차피 찍는 패턴이 반복되므로 각 문제번호를 수포자들의 패턴의 개수로 나눠주면 그 문제를 몇 번으로 찍었는지를 파악할 수 있다.
    #그를 토대로 맞았으면 1씩 더해줬다.
    if max(one_sol,two_sol,three_sol)==one_sol:
        winner.append(1)
    if max(one_sol,two_sol,three_sol)==two_sol:
        winner.append(2)
    if max(one_sol,two_sol,three_sol)==three_sol:
        winner.append(3)
    #동점자가 나올 수 있기 때문에 max로 한번에 뽑지 않고 각각의 점수가 최고점수와 같을 때 winner배열에 넣어줘서 return해주었다.
    return winner