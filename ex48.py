def primeNumber(n):
    if(n < 2): return False
    i = 2
    while(i*i <= n):
        if(n %i == 0): return False
        i += 1
    return True

def specialNumbers(n):
    for i in range(len(n)):
        tmp = int(n[i])
        if(primeNumber(i) and primeNumber(tmp) == False): return False
        elif(primeNumber(i) == False and primeNumber(tmp)): return False
    return True

t = int(input())
while(t > 0):
    n = input()
    if(specialNumbers(n)): print("YES")
    else: print("NO")
    t -= 1
