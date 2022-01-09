def solution(phone_book):
  phone_book.sort()    # 정렬을 해주면 앞부분이 비슷한 번호가 앞뒤로 위치하도록 만들 수 있다.
  i=0
  for j in range(i+1,len(phone_book)):
    if phone_book[j].find(phone_book[i])==0:
      # 개수를 새는 것이 아니기 때문에 단순히 양옆에 존재하는지만 확인해주면 된다. 
      return False
      i+=1
  return True