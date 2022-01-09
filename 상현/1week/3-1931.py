from collections import Counter

dic=Counter(input())
dic['sixnine']=0
for i in dic:
  if i=='6' or i=='9':
    dic['sixnine']+=dic[i]
if (dic['sixnine']%2==0):
  dic['sixnine']//=2
else:
  dic['sixnine']//=2
  dic['sixnine']+=1
dic['6']=0
dic['9']=0
card=0
for i in dic:
  if card<=dic[i]:
    card=dic[i]
print(card)