word = list(input())
for i in range(len(word)):
  change = ord(word[i]) - 3
  if change < ord('A'):
    change+=26
  word[i] = chr(change)
print(''.join(word))