def suma (n):
    s=0
    for i in range(1,n+1,2):
        s+=i
    return s
n=int(input("n="))
print(suma(n))
