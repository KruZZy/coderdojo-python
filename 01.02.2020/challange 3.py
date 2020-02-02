from random import randint
x = int(input("X: "))
f=[]
for i in range(x):
    f.append(randint(1,10000))
print(f)

k=int(input("k: "))
for i in f:
    if i%k==0:
        print(i)
