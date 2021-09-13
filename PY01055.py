def specialNumbers(n):
    if(len(n) % 2 == 0): return False
    if(n[0] == n[1]): return False
    tmp = n[0]
    leng = len(n)
    for i in range(0, leng, 2):
        if(n[i] != tmp): return False
    return True

t = int(input())
while(t > 0):
    n = input()
    if(specialNumbers(n)): print("YES")
    else: print("NO")
    t -= 1
