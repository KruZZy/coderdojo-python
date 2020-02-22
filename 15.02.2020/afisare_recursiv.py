def afisare(n):
    if n > 1: afisare(n-1)
    print(n)

x = int(input("x = "))
afisare(x)
