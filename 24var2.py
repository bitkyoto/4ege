with open('24_demo.txt') as f:
    f = f.readline()
    count = 0
    maxim = 0
    for i in range(len(f)-1):
        if f[i] != f[i+1]:
            count+=1
            if count >maxim:
                maxim = count
        else:
            count = 0
print(maxim+1)