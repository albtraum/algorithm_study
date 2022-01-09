#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer=[]
    for i in range(len(commands)):
        subarr=sorted(array[commands[i][0]-1:commands[i][1]])
        #조건1,2를 함께 넣었다. 배열의 인덱스가 0부터 시작하고 주어진 조건은 1부터 시작하므로 1을 빼줬다.
        answer.append(subarr[commands[i][2]-1])
        #위에서 만들 subarr에서 k번째 숫자를 구했다. 마찬가지로 1을 빼줬다.
    return answer