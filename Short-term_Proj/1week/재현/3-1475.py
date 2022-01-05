n = input() 
card = [0]*10 
c_6n9 = 0

for i in n:
    if(i=='6' or i=='9'): 
        c_6n9 += 1
    else:
        card[int(i)] += 1


if(c_6n9 % 2 == 0):
    c_6n9 = c_6n9//2
else:
    c_6n9 = c_6n9//2 + 1

card[6] = c_6n9

print(max(card))