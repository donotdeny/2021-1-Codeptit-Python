def prime(n):
    if(n < 2): return False
    i = 2
    while(i*i <= n):
        if(n % i == 0): return False
        i += 1
    return True

def checkHead(n):
    res = 0
    for i in range(0, 3):
        res = res*10 + int(n[i])
    if(prime(res)): return True
    return False

def checkTail(n):
    res = 0
    leng = len(n)
    for i in range(leng-3, leng):
        res = res*10 + int(n[i])
    if(prime(res)): return True
    return False

t = int(input())
while(t > 0):
    n = input()
    if(checkHead(n) and checkTail(n)): print("YES")
    else: print("NO")
    t -= 1
