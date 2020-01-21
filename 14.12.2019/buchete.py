#Lalelele din Parcul Soarelui au fost numerotate de la 1 la n.
#Se doreşte formarea unui buchet, care să conţină cel puţin o floare, iar două flori numerotate consecutiv să nu aparţină buchetului.
#Fiind dat n, numărul de flori, să se determine în câte moduri se poate forma buchetul.

n=int (input("n="))
f=[1,1]
for x in range (2,n+2):
    f.append (f[x-1]+f[x-2])
print(f[n+1]-1)
