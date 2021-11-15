word=input()
word=word.upper()
alphabet=list(set(word))
cnt_arr=[]
for i in alphabet:
  cnt_arr.append(word.count(i))
if cnt_arr.count(max(cnt_arr))>1:
  print("?")
else:
  print(alphabet[cnt_arr.index(max(cnt_arr))])