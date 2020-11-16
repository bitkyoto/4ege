def f(n,k,q):
    if n>k or n==q:
        return 0
    elif n==k :
        return 1
    else:
        return f(n+1,k,q)+ f(n*2,k,q)
print(f(1,10,5))