def gcd(a, b):
    if(b == 0): return a
    else: return gcd(b, a%b)

def prime(n):
    if(n < 2): return False
    i = 2
    while i*i <= n:
        if(n % i == 0):
            return False
        i += 1
    return True


def sumIsPrime(n):
    sum = 0
    while(n > 0):
        sum += n%10
        n = int(n / 10)
    if(prime(sum) == True): return True
    else: return False

t = int(input())
while(t > 0):
    arr = [int(i) for i in input().split()]
    ucln = gcd(arr[0], arr[1])
    if(sumIsPrime(ucln) == True): print("YES")
    else: print("NO")
    t -= 1
