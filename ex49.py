def primeNumber(n):
    if(n < 2): return False
    i = 2
    while(i*i <= n):
        if(n %i == 0): return False
        i += 1
    return True

def specialNumbers(n):
    leng = len(n)
    res = 0
    for i in range(leng-4, leng):
        res = res*10 + int(n[i])
    if(primeNumber(res)): return True
    return False

t = int(input())
while(t > 0):
    n = input()
    if(specialNumbers(n)): print("YES")
    else: print("NO")
    t -= 1
