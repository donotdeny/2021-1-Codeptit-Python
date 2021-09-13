from math import sqrt

def isPrime(n):
    if(n < 2): return False
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0): return False
    return True

def gcd(a, b):
    if(b == 0): return a
    else: return gcd(b, a%b)

t = int(input())
while(t > 0):
    res = 1
    n = int(input())
    for i in range(2, n):
        if(gcd(i, n) == 1): res += 1
    if(isPrime(res) == True): print("YES")
    else: print("NO")
    t -= 1
