n = 8
symbole = '*'

i = 1

for x in range(1, n+1):
    print(symbole*x)
for x in range(n-1, 0, -1):
    print(symbole*x)

# Optimized solution
# nombres = list(range(1, n+1)) + list(range(n-1, 0, -1))

# for x in nombres:
#     print(symbole*x)
