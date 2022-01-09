a = list(input())
for i in range(len(a)):
    x = ord(li[i]) - 3
    if x < 65:
        x += 26
    ans += chr(x)
print(ans)