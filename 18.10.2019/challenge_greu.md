# Veveritoiul ingroapa ghinde 

Veveritoiul are un teren de N*M metri patrati (un dreptunghi de N metri in jos si M in dreapta / N linii si M coloane de cate un metru fiecare) pe care ingroapa ghinde. Notam metrul patrat aflat la intersectia liniei **_i_** cu coloana **_j_** cu **_(i, j)_**. 
Pe fiecare metru patrat poate fi ingropat un numar infinit de ghinde. Veveritoiul, fiind un tip organizat, vrea ca distributia ghindelor sa fie cat mai buna pe terenul sau. 
Pentru asta, in fiecare secunda, timp de S secunde, va face urmatoarea operatie:
  - alege un metru patrat **_(x, y)_** 
  - ingroapa cate o ghinda pe **fiecare** metru patrat de pe linia **_x_**
  - ingroapa cate o ghinda pe **fiecare** metru patrat de pe coloana **_y_**
  
La final, el se intreaba: Pe cati metri patrati a ingropat un numar par de ghinde? 

## Ce se citeste (date de intrare):
In ordinea asta, N, M si S, pe rand.
Apoi cele S secunde: intai x, apoi y.

## La final, afisati raspunsul pentru acel test.

## Exemplu
```
2 2 3 (nota: N M S)
1 1 
1 2 
2 1
```

## Raspuns:
```
2
```

Dupa prima secunda, terenul arata asa:
| --- | --- |
| 2   |   1  |
| 1   |   0  |

Dupa a doua:

| --- | --- |
| 3   |   3  |
| 1   |   1  |

Iar dupa a 3-a:


| --- | --- |
| 4   |   3  |
| 3   |   2  |
