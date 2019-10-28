luni = ["Ianuarie","Februarie","Martie","Aprilie","Mai","Iunie",
"Iulie","August","Septembrie","Octombrie","Noiembrie","Decembrie"]
luna = int(input("Care este numarul lunii?"))
if luna>=1 and luna<=12:
    print(luni[luna-1])
else:print("Aceasta luna nu exista.")
