def gcd(a, b):
    if(b == 0): return a
    else: return gcd(b, a%b)

arr = [int(i) for i in input().split()]
n = arr[0]
k = arr[1]
j = 0
for i in range(10**(k-1), 10**k):
    if(j == 10):
        j = 0
        print()
    if(gcd(n, i) == 1): 
        print(i, end = " ")
        j += 1
