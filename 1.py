#####для поиска всех делителей
for x in range(568023,569230):
    count = 2
    for i in range(2,x//2+1):
        if x%i==0:
            count+=1
            if count==144:
                print(x)
