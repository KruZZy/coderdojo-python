def afisare(n):
    if n > 1: afisare(n-1)
    if n % 2 == 0:
        print(n)

n = int(input("n = "))
afisare(n)
