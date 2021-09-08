from math import sqrt

def isPrime(n):
    if(n < 2): return False
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0): return False
    return True


n = int(input())
condition = int(n/2)
arr = [int(i) for i in input().split()]
Hash = dict()
for i in range(n):
    if arr[i] in Hash.keys(): # arr[i] da nam trong Hash.keys()
        Hash[arr[i]] += 1
    else: 
        Hash[arr[i]] = 1
for i in range(n):
    if(isPrime(arr[i]) == False): continue
    key = 0
    for j in range(i):
        if(arr[i] == arr[j]): key = 1
    if(key == 1): continue
    print(arr[i], Hash[arr[i]])
