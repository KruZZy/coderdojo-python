ora_start=int(input("Ora="))
minut_start=int(input("Minute="))
durata_ore=int(input("Cate ore dureaza drumul="))
durata_minute=int(input("Cate minute dureaza drumul"))
ora_fin = ora_start+durata_ore
minute_fin = minut_start+durata_minute
if minute_fin>60:
    minute_fin%=60
    ora_fin+=1
print(ora_fin,minute_fin)
