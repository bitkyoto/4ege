a = []
for i in range(174457, 200000):
    b = []
    for x in range (2, int(i**(1/2))):
        if i % x == 0:
            b.append(x)
            b.append(i//x)
            if len(b)>2:
                break
        if len(b) ==2:
            a.append(b)

print(a)

for i in a:
    print(i)