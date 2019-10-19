from random import randint
N = int(input("Cate numere vrei sa iti adun?"))
suma = 0
numere = []
for x in range(N):
    numere.append(randint(0, 1000))
print(numere)
for x in numere:
    suma += x
print(suma)
