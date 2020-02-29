def afisare(n):
    if n% 2 == 1:
        print(n)
    if n > 1:
        afisare(n-1)
n = int(input("n="))
afisare(n)
