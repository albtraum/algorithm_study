def solution(board, moves):
  arr=[0]
  pop=0
  for num in moves:
    i=-1
    while i<len(board)-1:
      i+=1
      if board[i][num-1]!=0:
        if arr[-1]==board[i][num-1]:
          arr.pop()
          board[i][num-1]=0
          pop+=2
        else:
          arr.append(board[i][num-1])
          board[i][num-1]=0
          break
  return pop