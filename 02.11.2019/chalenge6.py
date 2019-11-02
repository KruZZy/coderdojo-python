from random import randint
n = int(input("n="))
lista = []
for x in range(n):
    lista.append(randint(1000,10000))

t = 0
for x in lista:
    t += x
print(t/n)
print(lista)
