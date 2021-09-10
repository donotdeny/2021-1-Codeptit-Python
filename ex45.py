def mulOfDigits(n):
    mul = 1
    for i in range(len(n)):
        if(n[i] == '0'): continue
        mul *= int(n[i])
    return mul

t = int(input())
while(t > 0):
    n = input()
    print(mulOfDigits(n))
    t -= 1
