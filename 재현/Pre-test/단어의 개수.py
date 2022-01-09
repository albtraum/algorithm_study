cnt = 0
sentence = input()
cnt_list = sentence.split()
for i in range(len(cnt_list)):
    if cnt_list[i] == ' ':
        continue
    else:
        cnt += 1
print(cnt)