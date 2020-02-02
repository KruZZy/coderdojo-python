n = int(input("n = "))
F = [0, 0, 1]
for i in range(3, n+1):
    F.append(F[i-1]+F[i-2])
print(F[n])
