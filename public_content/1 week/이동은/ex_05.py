#https://www.acmicpc.net/problem/1100
import sys
answer =0

#strip 으로 \n 제거, 8칸이기 때문에 8 넣음 
board = [sys.stdin.readline().strip() for i in range(8)]
#board = [line.rstrip('\n') for line in open('test.txt', 'r')]
#백준 txt est용

# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if ((i%2 ==0) and (j%2==0)) or ((i%2 ==1) and (j%2==1)):
#             if board[i][j] == 'F':
#                 answer+=1

print(answer)

#타인 코드 리뷰
'''
# 숏 코딩 
print('.'.join(eval('input(),'*8))[::2].count('F'))
-> eval('input(),'*8) -> eval 표현식, input(), 이라는 것을 8번 사용한 것
-> join : 문자열 합치는 함수, 앞에 있는 구분자 삽입 하면서 합침
-> [::2] : 두칸씩 추출 
-> F만 카운트 (2칸식 추출 하므로 남은건 흰색칸 위의 F뿐)
'''
