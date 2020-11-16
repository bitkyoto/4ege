#без указанания точки через которую НЕЛЬЗЯ ПРОХОДИТЬ

def f(n,k):
    if n>k:
        return 0
    elif  n==k:
        return 1
    else:
        return f(n+1, k)+f(n*3, k)

print(f(3,36))
#алгоритм для ситуации когда необходимо пройти через определенную точку
def f1(n,k):
    if n>k:
        return 0
    elif  n==k:
        return 1
    else:
        return f(n+1, k)+f(n*3, k)
print(f(3,10)*f(10,36))
#для ситуации в котором указана точку через которую НЕЛЬЗЯ ПРОЙТИ
def f2(n,k,q):
    if n>k or n==q:
        return 0
    elif n==k :
        return 1
    else:
        return f(n+1,k,q)+ f(n*2,k,q)
print(f(1,10,5))