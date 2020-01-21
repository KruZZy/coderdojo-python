def palindrom(L):
    i = 0
    j = len(L)-1
    while i != j: # i < j
        if L[i] != L[j]:
            return False
        i += 1
        j -= 1
    return True

from random import randint
n = int(input("n = "))
a = []
for i in range(n):
    a.append(randint(0, 8))
print(a)
if palindrom(a): print("e palindrom")
else: print("nu e palindrom")
