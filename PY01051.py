def sumOfDigits(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

def test(n):
    num = sumOfDigits(n)
    if(num < 10): return False
    tmp = num
    new = 0
    while(tmp > 0):
        new = new*10 + tmp%10
        tmp = int(tmp/10)
    if(new == num): return True
    return False

t = int(input())
while(t > 0):
    n = input()
    if(test(n) == True): print("YES")
    else: print("NO")
    t -= 1
