from random import randint
n =int(input("n = "))
A =[]
B =[]
for i in range (n):
    A.append(randint(1,20))
    B.append(randint(1,20))
print(A,B)
dist=0
for i in range (n):
    if A[i] != B[i]:
        dist+=1
print(dist)
