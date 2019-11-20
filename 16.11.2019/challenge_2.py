def sum(n):
    a = 0
    for b in range(1,n+1,4):
        a+=b*b # b ** 2
    return a
n = int(input('n='))
print(sum(n))
