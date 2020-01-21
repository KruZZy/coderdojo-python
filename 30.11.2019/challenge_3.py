n = int(input("n = "))
S = ['a', 'b']

for i in range(2, n+2):
    S.append(S[i-1] + S[i-2])

print(S[n])
