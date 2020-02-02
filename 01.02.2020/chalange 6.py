x=int(input("x="))
d=0
for i in range(2,x):
    if x%i==0:
        d=1
if d==1:
    print("numarul nu este prim")
else:
    print("numarul este prim")
