def solution(phone_book):
    answer = True
    hash_t = {}

    for number in phone_book:
        hash_t[number] = 0
    #숫자를 key값으로 넣음 

    for number in phone_book:
        temp = ""
        for bit in number:
            temp += bit
            if (temp in hash_t) and (temp != number):
                answer = False

    return answer
