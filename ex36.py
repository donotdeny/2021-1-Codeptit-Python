n = 1
while(n != 0):
    n = int(input())
    if(n == 1): print("1")
    elif(n != 0):
        Hash = dict()
        while(n != 1):
            if(n in Hash.keys()): Hash[n] += 1
            else: Hash[n] = 1
            if(n % 2 == 0):
                n = int(n/2)
            else:
                n = n*3 + 1
        print(len(Hash)+1)
