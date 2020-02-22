n = int(input("n = "))
prim = 1 # True
if n%2 == 0:
    prim = 0
else:
    i = 3
    while i*i <= n and prim == 0:
        if n%i == 0:
            prim = 0
        i += 2
if prim == 1:
    print("numarul este prim")
else: print("numarul nu este prim")
