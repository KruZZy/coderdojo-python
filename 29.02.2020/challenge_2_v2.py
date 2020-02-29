def afisare(n):
    print(n)
    if n > 1:
        afisare(n-2)

n = int(input("n="))
if n % 2 == 1:
    afisare(n)
else: afisare(n-1)
