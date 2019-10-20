# if si while 

## Expresiile logice
  Sunt expresiile care pot fi adevarate (notate cu True in Python) sau false (notate cu False in Python). Spre exemplu, sa luam doua number **_a_** si **_b_**, cu **_a < b_**
  ```python
  a == b # !!! = o singura data e pentru atribuiri, iar == e pentru verificare; expresia are valoarea False.
  a != b # a diferit de b, are valoarea True.
  a > b # a mai mare decat b, are valoarea False.
  a < b # a mai mic decat b, are valoarea True.
  a >= b # a mai mare sau egal decat b, are valoare False.
  a < b # a mai mic sau egal decat b, are valoarea True.
  a > b and a == b # a mai mare decat b si a egal cu b; asta ar avea valoarea False indiferent de valorile lui a si b.
  a > b or a == b # a mai mare decat b sau a e gal cu b; asta ar avea valoarea False in cazul nostru.
  ```

### Challenge-uri 

1. Cititi un numar in terminal (sa ii zicem N) si verificati daca e par sau impar. Daca e par, afisati mesajul 'par' si daca e impar, afisati mesajul 'impar'.
2. Cititi doua numere in terminal, sa zicem a si b. Determinati maximul dintre a si b.
3. Cititi 3 numere in terminal, sa spunem a, b si x. Verificati daca x apartine intervalului [a, b). (intervalul il contine pe a, dar nu si pe b).
4. Cititi din terminal o lista de numere. Afisati lista pana dati de un 0 in ea sau se termina.
5. Creati un program care ii cere utilizatorului sa introduca numarul unei luni (1, 2, ..., 12) si afiseaza numele lunii in cazul in care numarul e valid sau mesajul 'Aceasta luna nu exista!' daca numarul nu e intre 1 si 12.
6. Cititi un numar N in terminal. Afisati toate numerele pare intre 1 si N in ordine descrescatoare in doua moduri.
