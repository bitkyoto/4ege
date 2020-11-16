a = 7**10 + 8**22
s = ''
while a>0:
    s = str(a%5) + s
    a= a// 5
print(s)