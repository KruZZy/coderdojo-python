n = int(input("n = "))
F = [0] * (n+1)
F[0] = 1
F[1] = 1

def fibo(i):
    if F[i] == 0:
        F[i] = fibo(i-1) + fibo(i-2)
    return F[i]

print(fibo(n))
