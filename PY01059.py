def sumOfDigits(n):
    sum = 0
    for i in range(0, len(n), 2):
        sum += int(n[i])
    return sum

def check(n):
    for i in range(1, len(n), 2):
        if(n[i] != '0'): return True
    return False

def mulOfDigits(n):
    mul = 1
    for i in range(1, len(n), 2):
        if(n[i] != '0'):
            mul *= int(n[i])
    if(check(n) == False): mul = 0
    return mul

t = int(input())
while(t > 0):
    n = input()
    print(sumOfDigits(n), mulOfDigits(n))
    t -= 1
