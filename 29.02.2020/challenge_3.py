def suma(n):
    if n==1:
        return 1
    return n+suma(n-1)
n=int(input("n="))
print(suma(n))
