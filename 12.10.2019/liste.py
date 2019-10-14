lista = ["lapte", "ciocolata", "paine"]
print(lista)
lista.append("telefoane")
for x in lista:
    print(x)

lista.pop(0)
print(lista)
y = input("Ce vrei sa adaugi? ");
lista.append(y)
print(lista)
lista.append(input("Ce vrei sa mai adaugi?"))
print(lista)
