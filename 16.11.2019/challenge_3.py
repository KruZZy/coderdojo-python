def functie(l,n):
    for a in range(1,n+1):
        l.append(a**n)
list=[]
n = int(input("n = "))
functie(list,n)
print(list)
