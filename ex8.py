def ss(a, b, n):
    for i in range(n):
        if(a[i] > b[i]): return False
    return True

t = int(input())
while(t > 0):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    if(ss(a, b, n) == True): print("YES")
    else: print("NO")
    t -= 1
