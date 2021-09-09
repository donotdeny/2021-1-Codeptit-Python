def sumOfDigits(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

def test(n):
    num = sumOfDigits(n)
    if(num < 2): return False
    i = 2
    while(i*i <= num):
        if(num % i == 0): return False
        i += 1
    return True

t = int(input())
while(t > 0):
    n = input()
    if(test(n) == True): print("YES")
    else: print("NO")
    t -= 1
