kea = 0
with open ('24.txt') as f:
    for line in f:
        ka = 0
        ke = 0
        for a in line:
            if a =="E":
                ke+=1
            elif a =='A':
                ka +=1
        print(ka, ke)
        if ke>ka:
            kea+=1
print(kea)