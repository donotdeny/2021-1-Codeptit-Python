def sumOfDigits(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

def test(n):
    num = sumOfDigits(n)
    if(num % 3 == 0): return True
    else: return False

t = int(input())
while(t > 0):
    n = input()
    if(test(n) == True): print("YES")
    else: print("NO")
    t -= 1
