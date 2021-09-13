def gcd(a, b):
    if(b == 0): return a
    else: return gcd(b, a%b)

def getReverse(n):
    res = 0
    while(n > 0):
        res = res*10 + n%10
        n = int(n/10)
    return res

t = int(input())
while(t > 0):
    n = int(input())
    if(gcd(n, getReverse(n)) == 1): print("YES")
    else: print("NO")
    t -= 1
