def primeNumber(n):
    if(n < 2): return False
    i = 2
    while(i*i <= n):
        if(n %i == 0): return False
        i += 1
    return True

def sumOfDigits(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

def specialNumbers(n):
    if(primeNumber(sumOfDigits(n)) == False): return False
    for i in range(len(n)):
        tmp = int(n[i])
        if((i % 2 == 0) and (tmp % 2 != 0)): return False
        elif((i % 2 != 0) and(tmp % 2 == 0)): return False
    return True

t = int(input())
while(t > 0):
    n = input()
    if(specialNumbers(n)): print("YES")
    else: print("NO")
    t -= 1
