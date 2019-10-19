mesaj = input('Ce mesaj vrei sa (de)codezi? ')

rezultat = ''
i = len(mesaj) - 1
while i >= 0:
    rezultat += mesaj[i]
    i = i - 1

print(rezultat)
