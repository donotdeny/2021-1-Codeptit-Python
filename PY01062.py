def prime(n):
    if(n < 2): return False
    i = 2
    while(i*i <= n):
        if(n % i == 0): return False
        i += 1
    return True

def check(n):
    countPrime = 0
    normalNum = 0
    for i in range(len(n)):
        if(prime(int(n[i]))): countPrime += 1
        else: normalNum += 1
    if(countPrime > normalNum): return True
    return False

t = int(input())
while(t > 0):
    n = input()
    if(prime(len(n)) and check(n)): print("YES")
    else: print("NO")
    t -= 1
