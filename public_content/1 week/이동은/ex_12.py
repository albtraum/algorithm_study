#https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*4, reverse=True)
    answer =''
    
    for i in numbers:
        answer += i
    if answer[:1] == '0':
        answer = '0'
    return answer
