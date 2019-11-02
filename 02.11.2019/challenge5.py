from random import randint
n = int(input("n="))
k = int(input("k="))
c = 0
list = []
for x in range(n):
    list.append(randint(100, 1000))
for x in list:
    if x%k==0: c += 1
print(c)
print(list)
