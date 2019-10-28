def prod(n):
    p = 1
    for x in range(1,n+1):
        p*=x
    return p
print (prod (5))
