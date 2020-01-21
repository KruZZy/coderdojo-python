a=int(input('a='))
n=int(input('n='))
F=[]
for y in range(a):
    F.append(0)
F.append(1)

for y in range(a+1, n+2):
    F.append(F[y-1])
    for z in range(2,a+2):
        F[y] += F[y-z]
print(F)
