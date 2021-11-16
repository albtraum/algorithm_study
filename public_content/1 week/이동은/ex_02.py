def solution(array, commands):
    answer = []
    #자른 리스트에서, k 번째 수 
    for i,j,k in commands:
        answer.append((sorted(array[i-1:j]))[k-1])
    return answer
