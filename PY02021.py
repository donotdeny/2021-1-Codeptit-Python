t = int(input())
while(t > 0):
    arr = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    i, j, k = 0, 0, 0
    flag = 0
    # 1 5 10 20 40 80
    # 5 7 20 80 100
    # 3 4 15 20 30 70 80 120
    while(i < len(a) and j < len(b) and k < len(c)):
        if (a[i] == b[j] and b[j] == c[k]):
            flag = 1
            print(a[i], end = " ")
            i += 1
            j += 1
            k += 1
        elif(a[i] < b[j]): 
            i += 1
        elif(b[j] < c[k]):
            j += 1
        else: k += 1
    if(flag == 0): print("NO")
    else: print()
    t -= 1
