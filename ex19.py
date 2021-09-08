prime = [True for i in range(8000)]
res = []
p = 2
while (p*p <= 8000):
    if(prime[p] == True):
        for i in range(p*p, 8000, p):
            prime[i] = False
    p += 1
for p in range(2, 8000):
        if prime[p]: res.append(p)
arr = [int(i) for i in input().split()]
n = arr[0]
x = arr[1]
j = 0
for i in range(n+1):
    print(x, end = " ")
    x += res[j]
    j += 1
