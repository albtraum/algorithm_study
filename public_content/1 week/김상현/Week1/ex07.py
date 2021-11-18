word=input()
word=word.upper()
# 대/소문자 구분없기 때문에 하나로 통일하는데 출력을 대문자로 하므로 대문자로 바꿔준다.
alphabet=list(set(word))
# word에 있는 알파벳을 리스트에 넣어준다(중복X)
cnt_arr=[]
for i in alphabet:
  cnt_arr.append(word.count(i))
  # word에 알파벳마다 몇 개씩 있는지 넣어준다.
if cnt_arr.count(max(cnt_arr))>1:
  print("?")
  # max값이 여러개면 ?출력
else:
  print(alphabet[cnt_arr.index(max(cnt_arr))])
  # 아닐 경우 가장 큰 값이 있는 인덱스를 알파벳리스트에 넣어줘서 가장 많은 알파벳을 출력한다.