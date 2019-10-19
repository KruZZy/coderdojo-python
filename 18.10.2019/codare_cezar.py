mesaj = input("Ce mesaj vrei sa codezi? ")
cheie = int(input("Ce cheie vrei sa folosesti? "))


litere = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

alfabet = len(litere)
i = 0
cifrat = ''

def cod(mesaj, codez = 1):
    i = 0
    marime = len(mesaj)
    cif = ''
    while i < marime:
        nr = (litere.find(mesaj[i]) + codez * cheie) % alfabet
        if nr < 0: nr += alfabet
        cif += litere[nr]
        i += 1
    return cif

cifrat = cod(mesaj)
print(cifrat)
decifrat = cod(cifrat, -1)
print(decifrat)
