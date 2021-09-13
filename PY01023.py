t = int(input())
while(t > 0):
    n = int(input())
    i = 2
    res = "1 * "
    while(n > 1):
        count = 0
        if(n % i == 0):
            while(n % i == 0):
                count += 1
                n /= i
            res += str(i) + "^" + str(count) + " * "
        else: i += 1
    for i in range(len(res)-3):
        print(res[i], end = "")
    print()
    t -= 1
